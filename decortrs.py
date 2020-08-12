def decor(func1):
    def exec1():
        print("Hello")
        func1()
        print("Gelo")
    return exec1()
@decor
def sasa():
    print("lala")

sasa

