from typing import List, Tuple
import json


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


entries = [
    (1, "dummy_submission1", 426),
    (2, "dummy_submission2", 10),
    (3, "dummy_submission3", 200),
    (4, "dummy_submission4", 300),
    (5, "dummy_submission5", 400),
    (6, "dummy_submission6", 500),
    (7, "dummy_submission7", 600),
]


def main():
    html_str = open("index.html", "r").read()
    with open("data/eval_summary.json", "r") as f:
        entries = json.load(f)

    # Load original HTML
    with open("index.html", "r") as f:
        html_str = f.read()
    new_rows_str = generate_html_rows(entries)
    updated_html = update_html_autogen_rows(html_str, new_rows_str)
    # Save updated HTML
    with open("index.html", "w") as f:
        f.write(updated_html)


if __name__ == "__main__":
    main()
