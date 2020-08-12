import time
def Convert(string):
	li = list(string.split(","))
	return li
def typewords(arg,t):
    """In this function the letters are animated in the way that they supposed to be typed in a order
    Use- Put any word as argument but it should be string and separated by comma the string after comma is delayed 't' seconds
    where't' is second argument which should be in integer
    For example - If you want to type word HELLO in typewriter animation, then, Type string "H,L,L,O," and give time argument as
    't' seconds so the word H is typed imidiately and after 't' seconds the word E is typed and so on.
    Note- the words/letters/symbols separated by commas are only delayed."""
    kl=Convert(arg)
    for items in kl:
        print(items,end="")
        time.sleep(t)
    print("")
def star_pyramid1(x,t):
    while x>=0 :
        print(x*"*")
        x=x-1
        time.sleep(t)
        continue
def star_pyramid2(x,t):
    z=0
    while x>=0 :
        print(z*"*")
        z=z+1
        x=x-1
        time.sleep(t)
        continue
