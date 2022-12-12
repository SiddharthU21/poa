# Assertion error
# import sys
# assert('linux' in sys.platform),"Needs Linux system"


# try:
#     n1,n2=eval(input("Enter 2 nummbers : "))
#     result=n1/n2
#     print("Result: ",result)
#     if(n1==0): raise RuntimeError()
# except KeyboardInterrupt:
#     print("Keyboard Interrupt error")
# except ZeroDivisionError:
#     print("Division by zero")
# except SyntaxError:
#     print("Comma missing")
# except RuntimeError:
#     print("May be meaningless")
# except NameError:
#     print("Invalid input")
# except:
#     print("Something wrong in input")
# else: print("No exception")
# finally: print("Finally is called!")

# try:  
#     a = ['a', 'b', 'c']  
#     print (a[4])  
# except LookupError:  
#     print ("Index Error Exception Raised, list index out of range")

# try:
#     ny = 'Statue of Liberty'
#     my_list = [3, 4, 5, 8, 9]
#     print(my_list + ny)
# except TypeError:
#     print("Type error")

# User-defined Exception
class baseerror(Exception):
    pass
class lowvalue(Exception):
    pass
class highvalue(Exception):
    pass
value=30
while(1):
    try:
        n=int(input("Enter number : "))
        if n>value: 
            raise highvalue
        elif n<value: 
            raise lowvalue
        break
    except lowvalue:
        print("Low value. Enter value again!")
        print()
    except highvalue:
        print("High value. Enter value again!")
        print()
print("Right Number!")