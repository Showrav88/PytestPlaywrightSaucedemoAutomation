from pathlib import Path

file_path = Path(__file__).parent.parent / "resource" / "testdata.json"
print(file_path)
print(file_path.exists())
