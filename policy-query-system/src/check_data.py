from pathlib import Path

data_dir = Path(__file__).with_name("..") / "data"
for file in sorted(data_dir.glob("*.pdf")):
    print(file.name)