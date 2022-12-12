# # Built-in Functions
# # 1.Type conversion
# x=int(5.5)
# y=float(5)
# z=str(5)
# print(x,y,z)

# # 2.Type Coercion
# a=5.0/20
# print(a)
# b=5/20.5
# print(b)

# # 3.Mathematical Functions
# import math
# x=45
# r=x*math.pi/180
# print(math.sin(r))
# print(math.log10(x))

# # 4.Date and Time Functions
# import time
# t=time.localtime(time.time())
# n=time.asctime(t)
# print(n)

# # Calendar
# import calendar
# c=calendar.month(2022,9)
# print(c)

# # 5.Dir
# import os
# import math
# list=dir(math)
# print(list)

# # 6.Help
# import math
# help(math.cos)

# # User-defined Functions
# # 1.Square of a number
# def square(n):
#     return n**2
# x=int(input("Enter the number: "))
# print(square(x))

# # 2.Factorial using recursion
# def fact(x):
#     if(x==1):
#         return 1
#     return (x*fact(x-1))
# a=int(input("Enter the number: "))
# print(fact(a))

# # Anonymous Functions
# # 1.Lambda (Square)
# Square = lambda sq : sq**2
# print(Square(5))

# # 2.Map Function
# def square(n):
#     return n**2
# sq = map(square,range(6))
# print(list(sq))

# # 3.Filter (Odd Numbers)
# def odd(x):
#     if x%2==1:
#         return x
# lst=[1,2,3,4,5]
# odds=list(filter(odd,lst))
# print(odds)

# # 4. Reduce Function
# from functools import reduce
# nums=[1,2,3,4,5]
# s=reduce(lambda x,y:x+y,nums)
# print(s)

# # TOWER OF HANOI
def toh(d,s,a,t):
    if d==1:
        print('Move disk 1 from tower {} to tower {}'.format(s,t))
        return
    toh(d-1,s,t,a)
    print('Move disk {} from tower {} to tower {}'.format(d,s,t))
    toh(d-1,a,s,t)
d=int(input('Enter number of disks: '))
toh(d,'A','B','C')

# # Lambda function (greater of two number)
a=int(input('Enter a: '))
b=int(input('Enter b: '))
max=lambda a,b:a if a>b else b
print(f'{max(a,b)} is maximum number')

# # Using Map function perform element wise addition of elements of two lists
from operator import add
list1=[]
list2=[]
n1 = int(input("Enter number of elements in list 1 : "))
for i in range(0,n1):
    e1=int(input())
    list1.append(e1)
print(list1)
n2 = int(input("Enter number of elements in list 2 : "))
for i in range(0,n2):
    e2=int(input())
    list2.append(e2)
print(list2)
res=list(map(add,list1,list2))
print("The sum of elements in list : "+str(res))

# Using Map and Filter find the cube of all the odd numbers from the given input list
arr=[]
n = int(input("Enter the number of elements in list : "))
print("Enter list elements : ")
for i in range(0,n):
    arr.append(int(input()))
print(arr)
print("The cube of odd elements in list : ")
arr2=[]
arr2=list(map(lambda x:x**3,filter(lambda x:x%2!=0,arr)))
for i in arr2:
    print(i)