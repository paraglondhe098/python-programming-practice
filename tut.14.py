print("Enter month number")
import calendar as c
no=int(input())
if no<13:
    print(c.month_name[no])
else:
    print("Enter valid info")
