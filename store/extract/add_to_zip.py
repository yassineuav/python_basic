from pathlib import Path
from zipfile import ZipFile


with ZipFile("store/file.zip", "w") as zip:
    for path in Path().rglob("*.*"):
        zip.write(path)

with ZipFile("store/file.zip", "r") as zip:
    print(zip.namelist())
    info = zip.getinfo("store/file.zip")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("store/extract")
