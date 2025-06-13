import pandas as pd
import re
import os
import shutil
from urllib.parse import urlparse
from zipfile import ZipFile
from pathlib import Path

# 1. 解压 excel 文件
xlsx_path = "../tmp1.xlsx"
unzip_dir = "../unzipped_excel"
if os.path.exists(unzip_dir):
    shutil.rmtree(unzip_dir)
with ZipFile(xlsx_path, "r") as zip_ref:
    zip_ref.extractall(unzip_dir)

# 2. 提取 media 图片
media_dir = os.path.join(unzip_dir, "xl", "media")
output_img_dir = "../excel_images"
os.makedirs(output_img_dir, exist_ok=True)

media_images = sorted(Path(media_dir).glob("*.png"), key=lambda p: int(re.search(r'image(\d+)', p.stem).group(1)))
for i, img_path in enumerate(media_images):
    shutil.copy(img_path, f"{output_img_dir}/image{i+1}.png")

# 3. 读取 Excel 表格
df = pd.read_excel(xlsx_path)
df.columns = [col.strip() for col in df.columns]

# 4. 工具函数
def extract_date_with_fallback(link, time_value):
    if isinstance(link, str):
        match = re.search(r'arxiv\.org\/.*?\/(\d{4})', link)
        if match:
            yymm = match.group(1)
            return f"{yymm[:2]}-{yymm[2:]}"
        match_alt = re.search(r'20(\d{2})[-_.](\d{1,2})', link)
        if match_alt:
            yy = match_alt.group(1)
            mm = match_alt.group(2).zfill(2)
            return f"{yy}-{mm}"
    if isinstance(time_value, (str, float, int)):
        try:
            parts = str(time_value).strip().split(".")
            if len(parts) >= 2:
                yy = parts[0][-2:]
                mm = parts[1].zfill(2)
            else:
                yy = str(time_value)[-2:]
                mm = "01"
            return f"{yy}-{mm}"
        except:
            return "--"
    return "--"

def date_to_sort_key(date_str):
    if re.match(r"\d{2}-\d{2}", date_str):
        year, month = map(int, date_str.split("-"))
        return year * 12 + month
    return float("inf")

def format_link(link):
    return f"[link]({link})" if isinstance(link, str) and link.startswith("http") else "--"

def format_impact(link):
    if isinstance(link, str) and "github.com" in link:
        repo_path = urlparse(link).path.strip("/")
        return f"![Star](https://img.shields.io/github/stars/{repo_path}.svg?style=social&label=Star)"
    return "--"

# 5. 生成 markdown 表格
table_entries = []
for idx, row in df.iterrows():
    def safe_get(key):
        val = row.get(key, "")
        return str(val).strip() if pd.notna(val) and str(val).strip() else "--"

    paper_link = safe_get("Link-paper-page")
    time_value = row.get("Time", "")
    title_text = safe_get("Title")
    title = f"[{title_text}]({paper_link})" if paper_link.startswith("http") else title_text

    venue = safe_get("Conference").upper()
    date = extract_date_with_fallback(paper_link, time_value)
    code = format_link(safe_get("Code-link"))
    impact = format_impact(safe_get("Code-link"))
    benchmark = safe_get("Benchmark")

    # 图片插入 markdown
    img_md = f"![](excel_images/image{idx+1}.png)" if idx < len(media_images) else "--"

    row_data = [title, venue, date, code, impact, benchmark, img_md]
    table_entries.append((date_to_sort_key(date), row_data))

# 排序 & 生成表格 markdown
table_entries.sort(key=lambda x: x[0])
headers = ["Title", "Venue", "Date", "Code", "Impact", "Benchmark", "Illustration"]
markdown = "| " + " | ".join(headers) + " |\n"
markdown += "| " + " | ".join(["---"] * len(headers)) + " |\n"
for _, row in table_entries:
    markdown += "| " + " | ".join(row) + " |\n"

with open("../typora_ready_table.md", "w", encoding="utf-8") as f:
    f.write(markdown)
