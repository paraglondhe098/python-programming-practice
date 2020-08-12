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
    @staticmethod
    def printgood():
        return print("Hii")

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
print(Black_Widow.printgood())