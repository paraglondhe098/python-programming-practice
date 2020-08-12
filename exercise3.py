x= int(input("  Choose how many times do you want to print\n"))
y= int(input(" True or False "))

if y==0:
    while x>=0 :
        print(x*"$")
        x=x-1
        continue
if y==1:
    z=0
    while x>=0 :
        print(z*"%")
        z=z+1
        x=x-1
        continue



