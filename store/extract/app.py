from pathlib import Path

path = Path(r"C:\Users\Admin\Desktop\learn\python\standard library\main.py")

# path = path.with_name("test.py")

print("name: ", path.name)
print("stem: ", path.stem)
print("suffix: ", path.suffix)
print("parent: ", path.parent)
print("absolute: ", path.absolute())

print("is exist: ", path.exists())
print("is a file: ", path.is_file())
print("is a diractory: ", path.is_dir())

path = path.with_suffix(".py")
print(path)
