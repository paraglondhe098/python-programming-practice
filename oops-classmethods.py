class Avengers:
    Job="Superheroes"
    def details(self):
        return (f"Name is {self.name}, power is {self.power} and clolour is {self.colour}.")
    def changename(self,name):
        self.name=name
    def __init__(self,name,power,colour):
        self.name=name
        self.power=power
        self.colour=colour

    @classmethod
    def jobchange(cls,job):
        cls.Job=job
    @classmethod
    def Info(cls,str):
        return cls(*str.split("-"))

# Hulk=Avengers()
# Iron_Man=Avengers()
#
# Hulk.name ="Hulk"
# Hulk.power ="Smash"
# Hulk.colour="Green"
# Iron_Man.name="Iron man"
# Iron_Man.power="Intelligence"
# Iron_Man.colour="Red"
#  Avengers.Job="Villain"
# Iron_Man.jobchange("Villainee")
# print(Iron_Man.Job)
Black_Widow=Avengers.Info("Black Widow-Ninja-Black")
print(Black_Widow.name)
class Xmen(Avengers):
    def __init__(self,name,power,colour,rate):
        self.name=name
        self.power=power
        self.colour=colour
        self.xrating=rate

Wolverine=Xmen("Wolverine","Claws","Yellow",0.9)
print(Wolverine.details())
print(Wolverine.xrating)