import pandas as pd
import re
from urllib.parse import urlparse

file_path = "../tmp1.xlsx"
df = pd.read_excel(file_path)
df.columns = [col.strip() for col in df.columns]

def extract_arxiv_date(link):
    if isinstance(link, str):
        # arXiv 格式
        match = re.search(r'arxiv\.org\/.*?\/(\d{4})', link)
        if match:
            yymm = match.group(1)
            return f"{yymm[:2]}-{yymm[2:]}"
        # 其他格式中的 yyyy-mm, yyyy_mm 等
        match_alt = re.search(r'20(\d{2})[-_.](\d{1,2})', link)
        if match_alt:
            yy = match_alt.group(1)
            mm = match_alt.group(2).zfill(2)
            return f"{yy}-{mm}"
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

table_entries = []
for _, row in df.iterrows():
    def safe_get(key):
        val = row.get(key, "")
        return str(val).strip() if pd.notna(val) and str(val).strip() else "--"

    paper_link = safe_get("Link-paper-page")
    title_text = safe_get("Title")
    title = f"[{title_text}]({paper_link})" if paper_link.startswith("http") else title_text

    venue = safe_get("Conference").upper()
    date = extract_arxiv_date(paper_link)
    code = format_link(safe_get("Code-link"))
    impact = format_impact(safe_get("Code-link"))
    benchmark = safe_get("Benchmark")
    illustration = ""

    row_data = [title, venue, date, code, impact, benchmark, illustration]
    table_entries.append((date_to_sort_key(date), row_data))

table_entries.sort(key=lambda x: x[0])

headers = ["Title", "Venue", "Date", "Code", "Impact", "Benchmark", "Illustration"]
markdown = "| " + " | ".join(headers) + " |\n"
markdown += "| " + " | ".join(["---"] * len(headers)) + " |\n"
for _, row in table_entries:
    markdown += "| " + " | ".join(row) + " |\n"

with open("../typora_ready_table.md", "w", encoding="utf-8") as f:
    f.write(markdown)
