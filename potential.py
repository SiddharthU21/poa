def multipop(st, ele):
    for i in range(ele):
        if len(st) == 0:
            print("cannot pop element as stack is empty")
        else : 
            st.pop()

n = int(input("Enter number of elements: "))

print("Enter all", n, "elements:")
v = []
for i in range(n):
    v.append(int(input()))

st = []

print("Elements\tSize\tcost\tpotential\tamortized cost\tStack")

for i in range(n):
    count = 0
    siz = len(st) + 1
    siz_old = len(st)

    if v[i] <= siz:
        multipop(st, v[i])
        count += v[i]
        
    count += 1
    st.append(v[i])
    siz = len(st)
    # print("stack :",st)
    print(v[i],"\t\t",siz,'\t',count,'\t',(siz - siz_old),'\t\t',count + (siz - siz_old),'\t\t',st)
    print()




# Dynamic Table

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def potential(count, size):
    return 2 * count - size

size = 1
count = 0

arr = [0] * size

print("Dyanmic Tables")

print("Enter number of elements: ")
n = int(input())

print("Elements\tSize\tcost\tpotential\tamortized cost")

for i in range(1,n+1):
    if potential(count, size) <0:
        p_old = 0
    else:
        p_old = potential(count, size)
        
    if count < size:
        arr[count] = i
        count += 1
        pot = potential(count, size)
        cost = 1
    else:
        # double
        new_arr = [0] * (size * 2)
        for j in range(count):
            new_arr[j] = arr[j]
        arr = new_arr
        arr[count] = i
        size *= 2
        count += 1
        
        cost = i
        pot = potential(count, size)
  
        
    print(i,"\t\t",size,'\t',cost,'\t',pot,'\t\t',cost + pot - p_old)
    print()