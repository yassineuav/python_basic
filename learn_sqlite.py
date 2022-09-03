import sqlite3
import json
from pathlib import Path

# save data to sqlite
# movies = json.loads(Path("movies.json").read_text())
# # print(movies)

# with sqlite3.connect("db.sqlite3") as connect:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         connect.execute(command, tuple(movie.values()))
#     connect.commit()

# read data from db.sqlite

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
