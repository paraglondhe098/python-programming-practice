import time
class Emploee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.emaile = f"{fname}.{lname}@codewithary.com"
    def explain(self):
        return f"This if {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return print("Email not set")
        return f"{self.fname}.{self.lname}@codewithary.com"
    @email.setter
    def email(self,str):
        names = str.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname= names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
Parag=Emploee("Parag","Londhe")
# print(Parag.emaile)
Parag.fname="Charlie"
# print(Parag.emaile)
print(Parag.email)
Parag.email="CCa.MMA@gmail.com"
print(Parag.lname)
del Parag.email
print(Parag.email)