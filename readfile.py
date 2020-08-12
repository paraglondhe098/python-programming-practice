
i=0

while i<5:
    f = open("nen.txt", "a")
    k = input("Enter your name")
    i = i + 1
    f.write(str(i))
    f.write(")")
    f.write(k)
    f.write(" \n")
    f.close()
    print("Thank you", k)
    continue
print("Only 5 users can register")


