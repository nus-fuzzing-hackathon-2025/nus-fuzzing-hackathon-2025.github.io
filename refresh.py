from typing import List, Tuple
import json
import sys
import os


def generate_html_rows(data: List[Tuple[int, str, int]]) -> str:
    html_rows = []
    for no, submission_id, score in data:
        row = f"""
<tr>
    <td>{no}</td>
    <td>{submission_id}</td>
    <td>{score}</td>
</tr>
        """
        html_rows.append(row.strip())
    return "\n".join(html_rows)


def update_html_autogen_rows(html_str: str, new_rows: str) -> str:
    import re

    pattern = re.compile(
        r"(<!-- START_AUTOGEN_TABLE_ROWS -->)(.*?)(<!-- END_AUTOGEN_TABLE_ROWS -->)",
        re.DOTALL,
    )
    replacement = f"<!-- START_AUTOGEN_TABLE_ROWS -->\n{new_rows}\n<!-- END_AUTOGEN_TABLE_ROWS -->"
    return pattern.sub(replacement, html_str)


def main():
    if not os.path.exists("eval_summary.json"):
        sys.exit(1)
    if not os.path.exists("index.html"):
        sys.exit(1)

    html_str = open("index.html", "r").read()
    with open("eval_summary.json", "r") as f:
        entries = json.load(f)

    with open("index.html", "r") as f:
        html_str = f.read()

    new_rows_str = generate_html_rows(entries)
    print(new_rows_str)
    updated_html = update_html_autogen_rows(html_str, new_rows_str)
    with open("index.html", "w") as f:
        f.write(updated_html)


if __name__ == "__main__":
    main()
