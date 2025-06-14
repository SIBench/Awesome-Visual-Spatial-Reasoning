import pandas as pd
import re, os, shutil, random, string
from urllib.parse import urlparse
from zipfile import ZipFile
from pathlib import Path

# ---------- 1. 解压 Excel ----------
xlsx_path = "../tmp1.xlsx"
unzip_dir = "../unzipped_excel"
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

# 生成 8 位随机码（字母+数字+_-）
def rand_code(k: int = 8):
    chars = string.ascii_letters + string.digits + "_-"
    return "".join(random.choices(chars, k=k))

media_images = sorted(
    Path(media_dir).glob("*.png"),
    key=lambda p: int(re.search(r"image(\d+)", p.stem).group(1))
)

idx2filename = {}                                         # <idx> -> 随机文件名
for idx, img_path in enumerate(media_images):
    new_name = f"{rand_code()}.png"
    shutil.copy(img_path, f"{output_img_dir}/{new_name}")
    idx2filename[idx] = new_name                          # 保存映射

# ---------- 3. 读取 Excel 表格 ----------
df = pd.read_excel(xlsx_path)
df.columns = [col.strip() for col in df.columns]

# ---------- 4. 工具函数 ----------
def extract_date_with_fallback(link, time_value):
    if isinstance(link, str):
        m = re.search(r"arxiv\.org\/.*?\/(\d{4})", link)
        if m:
            yymm = m.group(1)
            return f"{yymm[:2]}-{yymm[2:]}"
        m2 = re.search(r"20(\d{2})[-_.](\d{1,2})", link)
        if m2:
            return f"{m2.group(1)}-{m2.group(2).zfill(2)}"
    if isinstance(time_value, (str, float, int)):
        parts = str(time_value).strip().split(".")
        yy = parts[0][-2:] if parts else str(time_value)[-2:]
        mm = parts[1].zfill(2) if len(parts) >= 2 else "01"
        return f"{yy}-{mm}"
    return "--"

def date_to_sort_key(date_str):
    return (
        lambda y, m: y * 12 + m
    )(*map(int, date_str.split("-"))) if re.match(r"\d{2}-\d{2}", date_str) else float("inf")

def format_link(link):
    return f"[link]({link})" if isinstance(link, str) and link.startswith("http") else "--"

def format_impact(link):
    if isinstance(link, str) and "github.com" in link:
        repo = urlparse(link).path.strip("/")
        return f"![Star](https://img.shields.io/github/stars/{repo}.svg?style=social&label=Star)"
    return "--"

# ---------- 5. 生成 Markdown ----------
table_entries = []
for idx, row in df.iterrows():
    g = lambda k: str(row.get(k, "")).strip() or "--"

    paper_link  = g("Link-paper-page")
    title_text  = g("Title")
    title       = f"[{title_text}]({paper_link})" if paper_link.startswith("http") else title_text
    venue       = g("Conference").upper()
    date        = extract_date_with_fallback(paper_link, row.get("Time", ""))
    code_link   = g("Code-link")
    code        = format_link(code_link)
    impact      = format_impact(code_link)
    benchmark   = g("Benchmark")

    # 🔑 这里！用随机文件名
    img_file = idx2filename.get(idx)
    img_md   = f"![](excel_images/{img_file})" if img_file else "--"

    row_data = [title, venue, date, code, impact, benchmark, img_md]
    table_entries.append((date_to_sort_key(date), row_data))


# 排序
table_entries.sort(key=lambda x: x[0], reverse=True)

# 拼 Markdown
headers = ["Title", "Venue", "Date", "Code", "Impact", "Benchmark", "Illustration"]
md  = "| " + " | ".join(headers) + " |\n"
md += "| " + " | ".join(["---"] * len(headers)) + " |\n"
for _, row in table_entries:
    md += "| " + " | ".join(row) + " |\n"

if os.path.exists("../typora_ready_table.md"):
    os.remove("../typora_ready_table.md")
Path("../typora_ready_table.md").write_text(md, encoding="utf-8")
