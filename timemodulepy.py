import time
y1=time.time()
for i in range(45000):
    print("I am good")
    continue
fortime=time.time()-y1
z=45000
y2= time.time()
while z>0:
    print("I am good")
    z=z-1
    continue
whiltime=time.time()-y2
print(fortime)
print(whiltime)
