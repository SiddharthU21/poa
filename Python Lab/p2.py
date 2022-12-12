print("Enter your name:-")
n = input()
print(type(n))

Area and Perimeter of Rectangle:-
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
print("Area = ",l*b)
print("Perimeter: ",l+b)

Square root
num = float(input("Enter the number: "))
print(pow(num,0.5))

for loop
for i in range(0,6):
    print(i)

l = ["Comp","IT","EXTC"]
for i in l:
    print(i,end=" ")
print()
d = dict()
d['r']=45
d['v']=18
for i in d:
    print("%s: %d"%(i,d[i]))

Pattern
for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    print()

Factorial of a number
n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

While loop
count=0
while(count<10):
    print(count,end=' ')
    count+=1

if elif else
num=64
if type(num)==int:
    print("Number is int")
elif type(num)==float:
    print("Number is float")
elif type(num)==set:
    print("Number is set")
elif type(num)==str:
    print("Number is str")
elif type(num)==tuple:
    print("Number is tuple")
elif type(num)==dict:
    print("Number is dictionary")
elif type(num)==list:
    print("Number is list")
else:
    print("Number is complex")

Odd and even
num=int(input())
if(num%2):
    print("Number is odd")
else:
    print("Number is even")

Fibonacci numbers
a=int(input())
fib1=0
fib2=1
if a==1: print(fib1,end=' ')
elif a==2: print(fib1,fib2,end=' ')
else:
    print(fib1,fib2,end=' ')
    for i in range(0,a-2):
        fib2=fib2+fib1
        fib1=fib2-fib1
        print(fib2,end=' ')

Leap year or not
b=int(input())
if b%4==0:
    if b%400==0: print("Leap year")
    else: print("Not a leap year")
else: print("Not a leap year")

Continue, Break and Pass
for i in "knowledge":
    if i == 'o' or i == 'd': continue
    print(i,end='')
print()
for i in "knowledge":
    if i == 'o' or i == 'd': break
    print(i,end='')
print()
for i in "knowledge":
    pass
print(i)

Appending in list, set and tuple
List=list()
l=int(input("Size of list: "))
print("Enter list elements: ")
for i in range(0,l):
    List.append(int(input()))
print(List)

Set=set()
s=int(input("Size of set: "))
print("Enter set elements: ")
for i in range(0,s):
    Set.add(int(input()))
print(Set)

T=(2,3,4,5)
print("Tuple before adding two element: ")
print(T)
L=list(T)
L.append(int(input("Enter new element: ")))
T=tuple(L)
print("Tuple after adding element: ")
print(T)

Swapping numbers
1. With Variable
a=int(input("Enter a: "))
b=int(input("Enter b: "))
temp=a
a=b
b=temp
print('a = ',a,'b = ',b,end=' ')
print()
2. Without Variable
a=int(input("Enter a: "))
b=int(input("Enter b: "))
a=a+b
b=a-b
a=a-b
print('a = ',a,'b = ',b,end=' ')