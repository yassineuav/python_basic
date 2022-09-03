from datetime import datetime
import time


print(time.time())

dt = datetime(2018, 1, 1)
# dt = datetime.now()
dt = datetime.strptime("2222-12-31", '%Y-%m-%d')
print(dt)
