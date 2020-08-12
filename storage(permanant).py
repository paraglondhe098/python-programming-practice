#This module is used to make a variable permanant by using file IO
try:
    import os
    os.mkdir("__Permanant_cache__")
except FileExistsError:
    pass
finally:
    import os
    import pickle
maindir = os.getcwd()
dir2 = os.path.join(maindir, "__Permanant_cache__")


def p_add(list_name,savefilename):
    """This function takes list/dict name as an argument and convert it into permanant binary form
    and save it into a {savelistname.pkl} file, where savelistname is the name of file(in str)
     in which you want to save your content."""
    filename = os.path.join(dir2, f"{savefilename}.pkl")
    fileopen=open(filename,"wb")
    pickle.dump(list_name,fileopen)
    fileopen.close()


def p_read(savefilename):
    # This function takes name of file you want to open as an argument and reads it for you and returns a list/dict
    filename = os.path.join(dir2, f"{savefilename}.pkl")
    fileopen=open(filename,"rb")
    list_return=pickle.load(fileopen)
    fileopen.close()
    return list_return


def gettime():
    import time
    localtime = time.asctime(time.localtime(time.time()))
    return localtime


def log(x):
    filename = os.path.join(dir2, f"Mylog.txt")
    z = open(filename, "a")
    z.write("At ")
    z.write(str(gettime()))
    z.write(f":=> {x} \n ")
    z.close()





