import requests
import pickle
r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
txt=r.text
content=txt.split("\n")
def func(str):
    z=str.split(",")
    return z
map_obj=map(func,content)
ls=list(map_obj)
ls.pop()
ls.pop()
file=open("exercise.pkl","wb")
pickle.dump(ls,file)
file.close()
file2=open("exercise.pkl","rb")
p=pickle.load(file2)
print(p)

