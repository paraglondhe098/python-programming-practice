
list1=[1,2,3,4]
# for i in range(len(list1)):
#     list1[i]=int(list1[i])
# z=list1[2]+1
# print(z)
# numbers = ["3", "34", "64"]
# # numbers = list(map(int, numbers))
#
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# z=numbers[2]+1
# def sq(a):
#     return a*a
# z=map(math.sinh,list1)
# print(list(z))
# func=[str]
# for i in range(4):
#     y= list(map(lambda x:x[i],func))
# print(y)
# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [square, cube]
# num = [2,3,5,6,76,3,3,2]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)
import functools
num = [2,3,5,6,76,3,3,2]
z= functools.reduce(lambda x,y:x*3+x**2+y**2+x+y,num)
print(z)
