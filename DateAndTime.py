
import time
import calendar
from datetime import date

# Sets time in seconds
ticks = time.time()
print(ticks)

# for localtime formats
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
print(time.localtime())
print()
# Text Calendar views
cal = calendar.month(2015, 11)
print(cal)
print()
print(calendar.month(2015, 12))

# shows week number
year = date.today().year  #sets current year
print(date(year, 11, 28).isocalendar()[1])

# Number of days to Christmas
today = date.today()
today = date.fromtimestamp(time.time())
christmas = date(today.year, 12, 25)
if christmas < today:
    christmas = christmas.replace(year=today.year + 1)
