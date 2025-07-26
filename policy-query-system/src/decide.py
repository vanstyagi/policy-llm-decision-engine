import os
import json
import re
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai
from retrieve import embed_chunks, top_chunks

# 0.  Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 1.  Helpers
def read_chunk(fname):
    return (
        Path(__file__).resolve().parent.parent / "outputs" / "chunks" / fname
    ).read_text(encoding="utf-8")

SYSTEM_PROMPT = """
You are an insurance policy assistant.
Use ONLY the provided excerpts below to answer.

Each excerpt is formatted as:
-----BEGIN filename.txt-----
<actual text>
-----END filename.txt-----

Return valid JSON:
{
  "decision": "approved" or "rejected",
  "amount": <int or null>,
  "justification": "...",
  "clauses": ["filename1.txt", "filename2.txt"]
}
"""

def sanitize_json(text: str):
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    return match.group(0) if match else "{}"

def decide(query_dict):
    chunk_embs = embed_chunks()
    query_str = (
        f"{query_dict['age']}yo {query_dict['gender']} "
        f"{query_dict['procedure']} {query_dict['location']} "
        f"{query_dict['policy_age_days']} days policy"
    )
    best = top_chunks(query_str, chunk_embs, k=3)

    context = ""
    for _, fname in best:
        text = read_chunk(fname)
        context += f"-----BEGIN {fname}-----\n{text}\n-----END {fname}-----\n"

    prompt = f"{SYSTEM_PROMPT}\n\n{context}\n\nQuery: {json.dumps(query_dict)}"

    model = genai.GenerativeModel("gemini-1.5-flash")
    raw = model.generate_content(prompt).text.strip()
    try:
        return json.loads(sanitize_json(raw))
    except json.JSONDecodeError:
        return {"decision": "error", "amount": None,
                "justification": raw, "clauses": []}

if __name__ == "__main__":
    sample = {
        "age": 46,
        "gender": "male",
        "procedure": "knee surgery",
        "location": "pune",
        "policy_age_days": 90
    }
    print(json.dumps(decide(sample), indent=2))