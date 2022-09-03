from pathlib import Path
from time import ctime

path = Path(r"store")

print(path.stat())

print(ctime(path.stat().st_ctime))

