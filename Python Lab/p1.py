#1. Text type
x1="Hello"
print(x1)
type(x1)

#2. Numeric type
x2=1
print(x2)
type(x2)
x3=1.2
print(x3)
type(x3)
x4=1.23
print(x4)
type(x4)
a = 9j
print(a)
print(type(a))

#Sequence type
list = ["DSA", "CP", 9, "Python"]
print(list)
print(type(list))

b = range(6)
print(b)
print(type(b))

c = range(3,9)
print(c)
print(type(c))

d =  range(9, 90, 10)
print(d)
print(type(d))

tuple = ("Python", "C", "C++", 8)
print(tuple)
print(type(tuple))

set = {"Operators", 9, "Data Types"}
print(set)
print(type(set))

#Dictionary
dict = {"Operators": 7, "Language": "Python"}
print(dict)
print(type(dict))

#binary
bin_value = b"toxic"
print(bin_value)
print(type(bin_value))

#null type
null = None
print(null)
print(type(null))

#Boolean type
boolean_value = True
print(boolean_value)
print(type(boolean_value))


#4. Operators

#4 i)Arithmetic
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#4 ii)Assignment
a=5
a+=2
print(a)
a-=1
print(a)
a*=5
print(a)
a/=2
print(a)
a//=5
print(a)
a%=10
print(a)
a**=5
print(a)

#4 iii)Comparison
x=2
y=5
print(x==y)
print(x>=y)
print(x<=y)
print(x!=y)
print(x>y)
print(x<y)

#4 iv)Logical
x=2
y=1
print(x>3 and y<1)
print(x>2 or y<5)
print(not(x>3 and y<1))

#4 v)Identity
x=3
y=1
print(x is y)
print(x is not y)

#4 vi)Membership
x=["DS","COMPS","IT"]
print("COMPS" in x)
print("EXTC" in x)
print("IT" not in x)

#4 vii)Bitwise
x=3
y=2
print(x&y)
print(x|y)
print(x^y)
print(~x)
print(x<<2)
print(x>>2)