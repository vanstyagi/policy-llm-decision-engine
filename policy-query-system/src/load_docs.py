from pathlib import Path
import PyPDF2

data_dir = Path(__file__).resolve().parent.parent / "data"

def load_pdf_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

for pdf_file in sorted(data_dir.glob("*.pdf")):
    full_text = load_pdf_text(pdf_file)
    print(f"{pdf_file.name}: {len(full_text)} characters")