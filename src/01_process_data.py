# src/process_data.py
import json
import gzip
from pathlib import Path
from typing import Iterable, Dict

def stream_arxiv_jsonl(path: str) -> Iterable[Dict]:
    """Yadi file gzipped json lines, adapt; else plain json list."""
    p = Path(path)
    if str(p).endswith(".gz"):
        with gzip.open(p, "rt", encoding="utf8") as f:
            for line in f:
                yield json.loads(line)
    else:
        # If it's a single big json list or jsonl, try line-by-line
        with open(p, "r", encoding="utf8") as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    # maybe single big list
                    f.seek(0)
                    data = json.load(f)
                    for item in data:
                        yield item
                    break

def filter_cs_subset(in_path: str, out_path: str, max_papers=20000):
    out = []
    for i, doc in enumerate(stream_arxiv_jsonl(in_path)):
        cats = doc.get("categories","")
        # simple filter: categories contain "cs."
        if "cs." in cats:
            out.append({
                "id": doc.get("id"),
                "title": doc.get("title"),
                "abstract": doc.get("abstract"),
                "categories": cats,
                "authors": doc.get("authors"),
                "update_date": doc.get("update_date"),
            })
        if len(out) >= max_papers:
            break
    import json
    with open(out_path, "w", encoding="utf8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(out)} CS papers to {out_path}")

if __name__ == "__main__":
    # example usage
    filter_cs_subset("data/arxiv-metadata-oai.json", "data/quantum_subset.json", max_papers=10000)
 