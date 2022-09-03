from pathlib import Path

path = Path("ecommerce")

print("is diractory exist", path.exists())

if not path.exists():
    print("creating dir ...")
    path.mkdir()
    print("done")
else:
    print("renaming ...")
    path.rename("store")
    print("done")

