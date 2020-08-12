def isa(n1,*args,**kwargs):
    j= n1+12
    for items,elements in args:
        print(items,elements)
        print("Goodbye")
    print("Now some thing")
    for jalebis,item in kwargs.items():
        print(f"{jalebis}is a best {item}")

k1=7
j1=[["kunal",8],["Mrunal",4]]
se1={"kunal":8,"Mrunal":4}
isa(k1,*j1,**se1)