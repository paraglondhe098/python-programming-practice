"""i=0
while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1,"Yes", end=" ")
    if(i==44):
        break
    i=i+1"""
print("Enter your no.")

while(True):
    i = int(input())
    if i>100:
        print("Congratulations you entered a number which is greater than 1oo")
        break
    if i<100:
        print("Try again")
        continue
