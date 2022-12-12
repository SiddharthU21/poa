# # Histogram
# def histogram(lst):
#     count=0
#     x=[]
#     k=[]
#     for i in range(len(lst)):
#         index=i
#         count=0
#         for j in range(index,len(lst)):
#             if lst[index] == lst[j] and lst[index] not in k:
#                 count = count + 1
#         k = k + [lst[index]]
#         if count!=0:
#             x = x + [(lst[index],count)]
#     x.sort()
#     x=sorted(x,key=lambda x:x[1])
#     return x
# print(histogram([13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7]))

# # Perfect Number
def perfect(n):
    sum=0
    for i in range(1, int(n/2)+1): 
        if n%i==0: sum+=i
    if sum==n: return True
print(perfect(28))

# Classes and objects
# class xyz:
#     x=2
#     y=4
# print(xyz.x)
# o1=xyz() # Object 
# print(o1.y)

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person('Ishan',21)
# print(p1.name)
# print(p1.age)

# # __init__ method
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print("Name : "+self.name)
#         print("Age : ",self.age)
# p1=person('Ishan',21)
# p1.myfunc()

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print("Name : "+self.name)
#         print("Age : ",self.age)
# p1=person('Ishan',21)
# p1.age=22
# p1.myfunc()

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print("Name : "+self.name)
#         print("Age : ",self.age)
# p1=person('Ishan',21)
# del p1
# print(p1)

# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# x=Person("Ishan","Madhani")
# x.printname()

# # Inheritance
# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# class Student(Person):
#     pass
# x=Student("Ishan","Madhani")
# x.printname()

# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# class Student(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname)
# x=Student("Ishan","Madhani")
# x.printname()

# # 4 different classes
# class employee:
#     role=''
#     def __init__(self,fname,lname,id):
#         self.fname=fname
#         self.lname=lname
#         self.id=id
#     def printn(self):
#         print(f'fname: {self.fname}')
#         print(f'lname: {self.lname}')
#         print(f'id: {self.id}')
#         print(f'role: {self.role}')
# class manager(employee):
#     devlist=[]
#     def __init__(self,fname,lname,id):
#         employee.__init__(self,fname,lname,id)
#         self.role='manager'
#     def add(self,e):
#         print("\nAdding employee:-\n")
#         e.printn()
#         if(e.role == 'developer' or 'tester'): self.devlist.append(e)
#     def remove(self,e):
#         print("\nRemoving employee:-\n")
#         e.printn()
#         if(e.role == 'developer' or 'tester'): self.devlist.remove(e)
#     def printlist(self):
#         print("\nList of employees:-\n")
#         for i in self.devlist:
#             print(f'fname: {self.fname}')
#             print(f'lname: {self.lname}')
#             print(f'id: {self.id}')
#             print(f'role: {self.role}')
#             print('\n')
# class developer(employee):
#     def __init__(self,fname,lname,id):
#         employee.__init__(self,fname,lname,id)
#         self.role='developer'
# class tester(employee):
#     def __init__(self,fname,lname,id):
#         manager.__init__(self,fname,lname,id)
#         self.role='tester'
# e1=developer("Ram","shah","2")
# e2=tester("Ishan","Madhani","1")
# e3=manager("Shyaam","Mehta","3")
# e3.printn()
# e3.add(e1)
# e3.add(e2)
# e3.remove(e1)
# e3.printlist()