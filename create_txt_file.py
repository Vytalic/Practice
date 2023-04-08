# practice creating files for data storage

from datetime import date
from datetime import datetime


today = date.today()
now = datetime.now()
with open('transactions.txt', 'w') as f:
    date2 = today.strftime("%B %d, %Y")
    current_time = now.strftime("%H:%M:%S")
    f.write("\n\n/---------------------------------------------\\")
    f.write("\n|         ")
    f.write(date2)
    f.write("     ")
    f.write(current_time)
    f.write("         |")
    f.write("\n\---------------------------------------------/\n\n")
   
print(today)