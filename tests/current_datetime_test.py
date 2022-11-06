from datetime import datetime

time=datetime.now().strftime(r'%H:%M:%S')
date=datetime.now().strftime(r'%Y/%m/%d')

print(time)
print(date)
