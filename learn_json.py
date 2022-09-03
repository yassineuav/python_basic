import json
from pathlib import Path


#ceate json
# movies = [
#     {"id":1, "title": "Limitless","year":2012},
#     {"id":2, "title": "Better than us","year":2020}
# ]

# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)
# print("data saved in movies.json file")

# read json

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"])
