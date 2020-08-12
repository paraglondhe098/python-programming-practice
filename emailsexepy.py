##Bhai baad me update kr skta hu..
import re
str1='''

Hello bro, my name is deepak tiwari and my email id is deepak@gmail.com,
And I am learning programming on code with harry youtube channel and I have one more
email:"deepak@dt.com"
and some more
email id:<dt@codewithharry.com>

email:"deepak@dt.com.in" and I have one more harrybhai@codewithharry.com.

'''
list1=re.findall(r'\w+@\S+\w',str1)

op=open("email_store.txt","a")

j=1
for i in list1:
    op.write(f"Email{j}:{i}\n")
    j=j+1
op.close()

print(f"Email's are:{list1}")
print(f"Total Email's are:{j-1}")