Ages=[["Parag",17],["Rohan",78],["Taheer",33],["Kunal",98],["Yuvraj",5],["jubin","pop"]]
for items,age in Ages:
    if str(age).isnumeric and int(age)>6:
        print(items, "is", age, "years old")
    else :
        exit(1)

