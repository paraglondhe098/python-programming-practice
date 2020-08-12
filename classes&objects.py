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

# Hulk = Avengers()
# Iron_Man=Avengers()

# Hulk.name ="Hulk"
# Hulk.power ="Smash"
# Hulk.colour="Green"
# Iron_Man.name="Iron man"
# Iron_Man.power="Intelligence"
# Iron_Man.colour="Red"
# Avengers.Job="Villain"
# print(Hulk.Job,Iron_Man.Job)
# print(Iron_Man.__dict__)
# Iron_Man.changename("I man")
# print(Iron_Man.name)
# Black_Panther=Avengers("Black panther","Vibranium","Black")
# print(Black_Panther.__dict__)