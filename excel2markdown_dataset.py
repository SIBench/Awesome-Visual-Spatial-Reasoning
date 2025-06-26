import pandas as pd
import re, os, shutil, random, string
from urllib.parse import urlparse
from zipfile import ZipFile
from pathlib import Path
from typing import Union

# ---------- 1. 解压 Excel ----------
xlsx_path = "../dataset.xlsx"
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

def rand_code(k: int = 8):
    chars = string.ascii_letters + string.digits + "_-"
    return "".join(random.choices(chars, k=k))

media_images = sorted(
    Path(media_dir).glob("*.png"),
    key=lambda p: int(re.search(r"image(\d+)", p.stem).group(1))
)

idx2filename = {}
for idx, img_path in enumerate(media_images):
    new_name = f"{rand_code()}.png"
    shutil.copy(img_path, f"{output_img_dir}/{new_name}")
    idx2filename[idx] = new_name

# ---------- 3. 读取 Excel 表格 ----------
df = pd.read_excel(xlsx_path).fillna("--")
df.columns = [col.strip() for col in df.columns]

# ---------- 4. 工具函数 ----------
def parse_time_value(time_value: Union[str, float, int]) -> str:
    s = str(time_value).strip()
    if not s or s == "--":
        return "--"
    m = re.search(r"20(\d{2})[.\-_/]?(\d{1,2})?", s)
    if m:
        yy = m.group(1)
        mm = m.group(2) or "1"
        return f"{yy}-{mm.zfill(2)}"
    m = re.search(r"(?<!\d)(\d{2})[.\-_/]?(\d{1,2})", s)
    if m:
        yy = m.group(1)
        mm = m.group(2)
        return f"{yy}-{mm.zfill(2)}"
    return "--"

def extract_date_with_fallback(paper_link: str, time_value: Union[str, float, int]) -> str:
    """优先从 arXiv 提取日期，否则从 Time 解析（支持两位/四位年份，默认 11 月）"""
    if isinstance(paper_link, str):
        links = re.split(r"[,\s]+", paper_link)
        for link in links:
            if "arxiv.org" in link:
                m = re.search(r"arxiv\.org\/.*?\/(\d{4})", link)
                if m:
                    yymm = m.group(1)
                    return f"{yymm[:2]}-{yymm[2:]}"
    
    s = str(time_value).strip()
    
    # 支持 2024、24 → 默认 11 月
    if re.fullmatch(r"\d{4}", s) and s.startswith("20"):
        return f"{s[2:]}-11"
    if re.fullmatch(r"\d{2}", s):
        return f"{s}-11"

    return parse_time_value(time_value)


def date_to_sort_key(date_str: str):
    if re.match(r"\d{2}-\d{2}", date_str):
        y, m = map(int, date_str.split("-"))
        return y * 12 + m
    return float("inf")

def format_citation(val: str) -> str:
    try:
        num = int(float(val))
        return str(num) if num >= 0 else "--"
    except:
        return "--"

# ---------- 5. 生成 HTML 表格 ----------
headers = ["Title", "Venue", "Date", "Download-Link", "Citation", "Input Type", "Illustration"]
col_widths = ["25%", "10%", "8%", "15%", "8%", "10%", "24%"]

table_rows = []
for idx, row in df.iterrows():
    g = lambda k: str(row.get(k, "--")).strip() or "--"
    
    # # ------- 5. 调试段开始 -------
    # target_title = "OpenEQA"        # 关键字，也可以用 idx==149 等

    # if target_title.lower() in g("Title").lower():
    #     print("="*60)
    #     print(f"[DEBUG] idx: {idx}")
    #     print(f"Title            : {g('Title')}")
    #     print(f"Link‑paper‑page  : {g('Link-paper-page')}")
    #     print(f"Time (raw)       : {g('Time')}")
        
    #     # 先计算 date，后面正式行也要用
    #     time_val = g("Time")
    #     date_dbg = extract_date_with_fallback(g("Link-paper-page"), time_val)
        
    #     print(f"Date (computed)  : {date_dbg}")
    #     print("="*60)
    # # ------- 5. 调试段结束 -------


    title_text  = g("Title")
    paper_link  = g("Link-paper-page")
    title       = f'<a href="{paper_link}">{title_text}</a>' if paper_link.startswith("http") else title_text

    venue       = g("Conference").upper()

    time_val    = g("Time")                      # ✅ 显式使用 g()，避免缺值
    date        = extract_date_with_fallback(paper_link, time_val)

    data_link   = g("Data-Link")
    download_link = f'<a href="{data_link}">link</a>' if data_link.startswith("http") else "--"

    citation    = format_citation(g("Cites"))
    input_type  = g("Input Type")

    img_file = idx2filename.get(idx)
    img_tag  = f'<img src="excel_images/{img_file}" alt="img" />' if img_file else "--"

    row_data = [title, venue, date, download_link, citation, input_type, img_tag]
    table_rows.append((date_to_sort_key(date), row_data))

# ---------- 6. 排序并拼接 HTML ----------
row_sorted = sorted(table_rows, key=lambda x: x[0], reverse=True)

html  = "<table>\n<colgroup>\n" + "\n".join([f"  <col style=\"width: {w}\">" for w in col_widths]) + "\n</colgroup>\n"
html += "<thead>\n<tr>\n" + "\n".join([f"  <th>{h}</th>" for h in headers]) + "\n</tr>\n</thead>\n<tbody>\n"

for _, row in row_sorted:
    html += "  <tr>\n" + "\n".join([f"    <td>{cell}</td>" for cell in row]) + "\n  </tr>\n"
html += "</tbody>\n</table>\n"

# ---------- 7. 写入文件 ----------
md_path = "../typora_ready_table.md"
Path(md_path).write_text(html, encoding="utf-8")

print("✅ HTML 格式的 Markdown 表格已生成:", md_path)
