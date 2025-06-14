import pandas as pd
import re, os, shutil, random, string
from urllib.parse import urlparse
from zipfile import ZipFile
from pathlib import Path
from typing import Union

# ---------- 1. 解压 Excel ----------
xlsx_path = "../tmp1.xlsx"           # 原始 .xlsx 文件
unzip_dir = "../unzipped_excel"      # 临时解压目录
if os.path.exists(unzip_dir):
    shutil.rmtree(unzip_dir)
with ZipFile(xlsx_path, "r") as zip_ref:
    zip_ref.extractall(unzip_dir)

# ---------- 2. 处理 media 图片 ----------
media_dir      = os.path.join(unzip_dir, "xl", "media")
output_img_dir = "../excel_images"
if os.path.exists(output_img_dir):
    shutil.rmtree(output_img_dir)
os.makedirs(output_img_dir, exist_ok=True)

def rand_code(k: int = 8):
    """生成 k 位随机字符串（字母+数字+_-）"""
    chars = string.ascii_letters + string.digits + "_-"
    return "".join(random.choices(chars, k=k))

media_images = sorted(
    Path(media_dir).glob("*.png"),
    key=lambda p: int(re.search(r"image(\d+)", p.stem).group(1))
)

idx2filename = {}                       # <行索引> -> 随机文件名
for idx, img_path in enumerate(media_images):
    new_name = f"{rand_code()}.png"
    shutil.copy(img_path, f"{output_img_dir}/{new_name}")
    idx2filename[idx] = new_name

# ---------- 3. 读取 Excel 表格 ----------
df = (
    pd.read_excel(xlsx_path)            # 读 Excel
      .fillna("--")                     # 所有 NaN → "--"
)
df.columns = [col.strip() for col in df.columns]

# ---------- 4. 工具函数 ----------

def parse_time_value(time_value: Union[str, float, int]) -> str:
    """将 Time 列内容解析成 'yy-mm'；支持以下形式：
    - 2025-06  /  2025.6  / 202506
    - 25-06    /  25.6    / 2506
    解析失败返回 '--'."""
    s = str(time_value).strip()
    if not s or s == "--":
        return "--"

    # 1) 4 位年份，以 20xx 开头
    m = re.search(r"20(\d{2})[.\-_/]?(\d{1,2})?", s)
    if m:
        yy = m.group(1)
        mm = m.group(2) or "1"
        return f"{yy}-{mm.zfill(2)}"

    # 2) 2 位年份（假设 2000 年以后），如 25-06 或 2506
    m = re.search(r"(?<!\d)(\d{2})[.\-_/]?(\d{1,2})", s)
    if m:
        yy = m.group(1)
        mm = m.group(2)
        return f"{yy}-{mm.zfill(2)}"

    return "--"

def extract_date_with_fallback(link: str, time_value: Union[str, float, int]) -> str:
    """1. 若 link 是 arXiv，则从 link 中提取 yy-mm；否则解析 Time 列"""
    if isinstance(link, str) and "arxiv.org" in link:
        m = re.search(r"arxiv\.org\/.*?\/(\d{4})", link)
        if m:
            yymm = m.group(1)               # e.g. '2307'
            return f"{yymm[:2]}-{yymm[2:]}" # '23-07'
    return parse_time_value(time_value)

def date_to_sort_key(date_str: str):
    """把 'yy-mm' 转成可排序整数，非标准日期返回 inf"""
    if re.match(r"\d{2}-\d{2}", date_str):
        y, m = map(int, date_str.split("-"))
        return y * 12 + m
    return float("inf")

def format_code_link(link):
    return f'<a href="{link}">link</a>' if isinstance(link, str) and link.startswith("http") else "--"

def format_impact(link):
    if isinstance(link, str) and "github.com" in link:
        repo = urlparse(link).path.strip("/")
        return f'<img src="https://img.shields.io/github/stars/{repo}.svg?style=social&label=Star" alt="Star count" />'
    return "--"

def wrap_benchmark(text: str, max_items: int = 2) -> str:
    """Benchmark 列：每行至多 max_items 项，用 <br> 分行"""
    if text == "--":
        return text
    parts = [p.strip() for p in text.split(",") if p.strip()]
    lines = [", ".join(parts[i:i+max_items]) for i in range(0, len(parts), max_items)]
    return "<br>".join(lines)

# ---------- 5. 生成 HTML 表格 ----------
headers    = ["Title", "Venue", "Date", "Code", "Impact", "Benchmark", "Illustration"]
col_widths = ["25%", "10%", "8%", "10%", "10%", "7%", "30%"]  # 固定列宽

table_rows = []
for idx, row in df.iterrows():
    g = lambda k: str(row.get(k, "--")).strip() or "--"

    paper_link  = g("Link-paper-page")
    title_text  = g("Title")
    title = f'<a href="{paper_link}">{title_text}</a>' if isinstance(paper_link, str) and paper_link.startswith("http") else title_text

    venue     = g("Conference").upper()
    date      = extract_date_with_fallback(paper_link, row.get("Time", "--"))
    code_link = g("Code-link")
    code      = format_code_link(code_link)
    impact    = format_impact(code_link)
    benchmark = wrap_benchmark(g("Benchmark"))

    img_file = idx2filename.get(idx)
    img_tag  = f'<img src="excel_images/{img_file}" alt="img" />' if img_file else "--"

    row_data = [title, venue, date, code, impact, benchmark, img_tag]
    table_rows.append((date_to_sort_key(date), row_data))

# ---------- 6. 排序并拼接 HTML ----------
row_sorted = sorted(table_rows, key=lambda x: x[0], reverse=True)

html  = "<table>\n<colgroup>\n" + "\n".join([f"  <col style=\"width: {w}\">" for w in col_widths]) + "\n</colgroup>\n"
html += "<thead>\n<tr>\n" + "\n".join([f"  <th>{h}</th>" for h in headers]) + "\n</tr>\n</thead>\n<tbody>\n"

for _, row in row_sorted:
    html += "  <tr>\n" + "\n".join([f"    <td>{cell}</td>" for cell in row]) + "\n  </tr>\n"
html += "</tbody>\n</table>\n"

# ---------- 7. 写入文件 ----------
md_path = "../typora_ready_table.md"   # 输出 HTML 的 .md 文件
Path(md_path).write_text(html, encoding="utf-8")

print("✅ HTML 格式的 Markdown 表格已生成:", md_path)
