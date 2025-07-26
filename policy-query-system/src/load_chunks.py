from pathlib import Path
import json

chunks_dir = Path(__file__).resolve().parent.parent / "outputs" / "chunks"

def load_all_chunks():
    """Return a dict {filename: text} for every .txt chunk."""
    chunks = {}
    for txt_file in sorted(chunks_dir.glob("*.txt")):
        chunks[txt_file.name] = txt_file.read_text(encoding="utf-8")
    return chunks

if __name__ == "__main__":
    all_chunks = load_all_chunks()
    print(json.dumps(list(all_chunks.keys())[:5], indent=2))   # show first 5 keys
    print(f"Total chunks loaded: {len(all_chunks)}")