import csv
import re
from pathlib import Path


def _normalize_header(name: str) -> str:
    text = name.strip()
    if text == "*** Test Cases ***":
        return "case_name"
    text = text.replace("${", "").replace("}", "")
    text = re.sub(r"\s+", "_", text)
    return text.lower()


def load_scenario_data(csv_path: Path) -> list[dict]:
    rows: list[dict] = []
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=";")
        normalized = [_normalize_header(col) for col in reader.fieldnames or []]
        for index, raw in enumerate(reader, start=1):
            cleaned = {}
            for old, new in zip(reader.fieldnames or [], normalized):
                cleaned[new] = (raw.get(old) or "").strip()
            cleaned["user_index"] = index
            rows.append(cleaned)
    return rows

