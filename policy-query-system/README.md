# 🛡️ POLICY-QUERY-SYSTEM  
**End-to-End LLM Decision Engine for Insurance, Legal & HR Docs**  
*Hackathon-Ready | Gemini-Powered | PDF-to-Decision in Seconds*

---

## 🚀 QUICK DEMO 

```bash
git clone https://github.com/vanstyagi/policy-llm-decision-engine.git
cd policy-query-system
pip install -r requirement.txt
echo "GEMINI_API_KEY=YOUR_KEY_HERE" > .env
python src/main.py "46-year-old male, knee surgery in Pune, 3-month policy"
```

✔️ Output will show in terminal and `outputs/final.json` like:

```json
{
  "decision": "approved",
  "amount": null,
  "justification": "Knee surgery is covered. Age & location are valid per policy clauses.",
  "clauses": ["data_chunk95.txt", "data4_chunk56.txt", "data_chunk52.txt"]
}
```

---

## 📦 PROJECT STRUCTURE

| **Folder / File**        | **Purpose**                                   |
|--------------------------|-----------------------------------------------|
| **data/**                | Input folder for PDF / DOCX / EML             |
| **outputs/chunks/**      | Auto-generated document chunks (300 words)    |
| **outputs/final.json**   | Final structured JSON output                  |
| **src/check_data.py**    | List available documents                      |
| **src/chunk_docs.py**    | Split documents into chunks                   |
| **src/load_docs.py**     | Extract raw text                              |
| **src/load_chunks.py**   | Load all chunk files                          |
| **src/parse_query.py**   | Parse natural query → structured JSON         |
| **src/retrieve.py**      | Semantic search via sentence-transformers     |
| **src/decide.py**        | LLM (Gemini) generates decision JSON          |
| **src/main.py**          | CLI entry point for full pipeline             |
| **.env**                 | Store API Key (never commit)                  |
| **requirement.txt**      | All dependencies                              |
| **README.md**                                      

---

## ⚙️ INSTALLATION & USAGE

| 🧩 Step         | 🛠️ Command             |
| 1️⃣ Clone        | `git clone <repo-url>` |
| 2️⃣ Install Deps | `pip install -r requirement.txt` |
| 3️⃣ Set API Key  | `echo "GEMINI_API_KEY=YOUR_KEY" > .env` |
| 4️⃣ Run          | `python src/main.py "<your query>"` |
| 5️⃣ Output       | `cat outputs/final.json` |

---

## ✅ FEATURE CHECKLIST

| Capability                              | ✅ Status |
|----------------------------------------|------------|
| Natural-language query (free-text)     | ✅        |
| Parse age, gender, location, procedure | ✅        |
| Ingest PDF, DOCX, and EML              | ✅        |
| Semantic search using embeddings       | ✅        |
| Gemini-based approve/reject reasoning  | ✅        |
| Clause-level mapping                   | ✅        |
| JSON output for downstream usage       | ✅        |

---

## 💬 SAMPLE QUERIES

```bash
python src/main.py "46-year-old male, knee surgery in Pune, 3-month policy"
python src/main.py "23-year-old female, cardiac surgery, Mumbai, 6-month policy"
python src/main.py "60-year-old man, hip replacement, Delhi, 1-year policy"
```

---

## 🧠 TECH STACK

- **Python 3.11**
- **PyPDF2**, **python-docx** – document ingestion
- **Sentence-Transformers** – semantic similarity search
- **Google Gemini 1.5 Flash** – final decision reasoning
- **dotenv** – key management

---

## 🔄 PIPELINE OVERVIEW

| 🧩 Stage             |     🔍 Description                         |
|----------------------|---------------------------------------------|
| **parse_query.py**   | Regex / NLP → extract query entities |
| **retrieve.py**      | Embed + semantic search over document chunks |
| **decide.py**        | Gemini generates final structured JSON |
| **final.json**       | Output → usable by any downstream system |

🧾 **Flow:**

```text
Plain-English Query
        ↓
parse_query.py
        ↓
retrieve.py (embedding + search)
        ↓
decide.py (LLM reasoning)
        ↓
final.json
```

---

## 📜 LICENSE

MIT © VANSH TYAGI

---
