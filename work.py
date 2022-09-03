from pathlib import Path

path = Path(r"C:\Program Files")


paths = [p for p in path.iterdir() if p.is_dir()]

py_files = [p for p in path.rglob("*.py")]

print(py_files)
