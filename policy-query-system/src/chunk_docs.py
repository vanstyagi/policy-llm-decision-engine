from pathlib import Path
import PyPDF2

data_dir   = Path(__file__).resolve().parent.parent / "data"
chunks_dir = Path(__file__).resolve().parent.parent / "outputs" / "chunks"
chunks_dir.mkdir(parents=True, exist_ok=True)

def chunk_pdf(pdf_path, words_per_chunk=300):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += (page.extract_text() or "") + " "

    words = text.split()
    for i in range(0, len(words), words_per_chunk):
        chunk = " ".join(words[i:i+words_per_chunk])
        out_file = chunks_dir / f"{pdf_path.stem}_chunk{i//words_per_chunk}.txt"
        out_file.write_text(chunk, encoding="utf-8")

for pdf in sorted(data_dir.glob("*.pdf")):
    chunk_pdf(pdf)
    print(f"Chunked {pdf.name}")