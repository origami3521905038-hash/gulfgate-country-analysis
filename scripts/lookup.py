"""Offline read-only lookup for GulfGate terminology and structured records."""
from pathlib import Path
import argparse
import csv
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
TERMS = ROOT / "assets" / "terms.csv"
RECORDS = ROOT / "references" / "knowledge" / "records.jsonl"


def _records(path):
    with path.open(encoding="utf-8-sig") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def retrieve(kind, query, country="", industry="", topic="", record_kind="", limit=8):
    if limit < 1:
        raise ValueError("limit must be positive")
    if not query.strip():
        raise ValueError("query must not be empty")
    results = []
    needle = query.casefold()
    if kind == "term":
        with TERMS.open(encoding="utf-8-sig", newline="") as handle:
            for row_number, row in enumerate(csv.DictReader(handle), 1):
                body = "\n".join(str(value) for value in row.values())
                if needle in body.casefold():
                    results.append({"row": row_number, **row})
    else:
        for record in _records(RECORDS):
            if country and record.get("country") != country:
                continue
            if industry and record.get("industry") != industry:
                continue
            if topic and topic not in record.get("topics", []):
                continue
            if record_kind and record.get("kind") != record_kind:
                continue
            keys = ("id", "title", "claim", "guidance", "question", "evidence", "pitfall", "scope", "official_ids", "url")
            body = "\n".join(str(record.get(key, "")) for key in keys)
            matched = record.get("id", "").casefold() == needle if kind == "record" else needle in body.casefold()
            if matched:
                results.append(record)
    return {
        "query": query,
        "matches": len(results),
        "returned": min(limit, len(results)),
        "truncated": len(results) > limit,
        "notice": "本地命中仅为研究线索，不代表当前外部核验。",
        "results": results[:limit],
    }


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=["record", "search", "term"])
    parser.add_argument("query")
    parser.add_argument("--country", default="", choices=["", "SA", "AE", "QA", "KW", "BH", "OM"])
    parser.add_argument("--industry", default="", choices=["", "I1", "I2", "I3", "I4", "I5"])
    parser.add_argument("--topic", default="", choices=[""] + [f"M{i}" for i in range(1, 8)])
    parser.add_argument("--record-kind", default="")
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()
    if args.kind == "term" and any((args.country, args.industry, args.topic, args.record_kind)):
        parser.error("term lookup does not use record filters")
    payload = retrieve(args.kind, args.query, args.country, args.industry, args.topic, args.record_kind, args.limit)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
