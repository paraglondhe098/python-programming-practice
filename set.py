s=set([1,2,3,4])

s.add(5)

s1=s.difference(([1,2,6]))
s2=([6,7])

s.remove(3)
print(s.isdisjoint(s2))
