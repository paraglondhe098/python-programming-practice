print("___*Guess the number*___")
print("Total no. of guesses are 9")
x=55
z=9
while z>0 :
    z=z-1
    y=int(input("The no. is  "))
    if y==x :
        print("Congrats! Your guess was right, You won the game")
        print("You took",9-z,"No. of guesses .")
        break
    if 55 < y < 61:
        print("You are too close reduce a little bit")
        print("trials left",z)
        continue
    if 61 < y < 71:
        print("You are close reduce more")
        print("trials left", z)
        continue
    if 71  < y < 91:
        print("Reduce more")
        print("trials left", z)
        continue
    if 91 < y < 111:
        print("Reduce, you are too far from the no.")
        print("trials left", z)
        continue
    if 49 < y < 55:
        print("You are too close add a little bit")
        print("trials left", z)
        continue
    if 39 < y < 49:
        print("You are close add more")
        print("trials left", z)
        continue
    if 19 < y < 39:
        print("Add more")
        print("trials left", z)
        continue
    if 0 < y < 19:
        print("Add more, you are too far prom the no.")
        print("trials left", z)
        continue
if z==0:
    print("Sorry, but trials are finished")
    print("Game over")