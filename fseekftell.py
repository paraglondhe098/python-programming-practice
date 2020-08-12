f=open("nen.txt")

f.seek(4)
print(f.tell())
print(f.readline())
f.close()