d1 = {"Parag":"Ice cream", "Rohan":"Barfi","Karan":"Jalebi","Charlie":{"Breakfast":("Cold Drink","Water")}}
d1["Chanchal"]="bhindi"
d2=d1.copy()
del d2["Karan"]
#print(d2)
#print (d1)
d2.update({"Rahul":"Farsan"})
print(d2)