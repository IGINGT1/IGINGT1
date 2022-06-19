import datetime
import sys

def calendar(y = 1990, m = 11, d = 6):
    print(datetime.date(y, m, d))

if len(sys.argv) > 2:
    calendar(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]) )
else:
    calendar()