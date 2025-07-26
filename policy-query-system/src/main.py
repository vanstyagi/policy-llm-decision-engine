import sys
import json
from pathlib import Path
from parse_query import parse_query
from decide import decide

if __name__ == "__main__":
    # Allow either a command-line arg OR a default demo query
    raw = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else \
          "46-year-old male, knee surgery in Pune, 3-month-old insurance policy"

    parsed = parse_query(raw)
    result = decide(parsed)

    # Pretty print + save to outputs/final.json
    print(json.dumps(result, indent=2, ensure_ascii=False))
    Path("outputs/final.json").write_text(json.dumps(result, indent=2), encoding="utf-8")