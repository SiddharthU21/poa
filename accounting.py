account = 0

def multipop(st, ele):
    for i in range(ele):
        if len(st) == 0:
            print("cannot pop element as stack is empty")
        else : 
            # print("Popped:", st.pop())
            st.pop()

n = int(input("Enter number of elements: "))

print("Enter all", n, "elements:")
v = []
for i in range(n):
    v.append(int(input()))

st = []

print("Elements\tSize\tcost\tamortized cost\tbank")

for i in range(n):
    count = 0
    siz = len(st) + 1

    if v[i] <= siz:
        multipop(st, v[i])
        count += v[i]
        account -= v[i]

    count += 1
    account += 2
    account -= 1
    st.append(v[i])
    siz = len(st)
    print(v[i],"\t\t",siz,'\t',count,'\t\t2\t',account)
    print()




# Dynamic Table

size = 1
count = 0
arr = [0] * size
account = 0
print("Dyanmic Tables")

print("Enter number of elements: ")
n = int(input())

print("Elements\tSize\tcost\tamortized cost\tbank")

for i in range(1,n+1):
    account += 3  # adding 3 to the account

    if count < size:
        arr[count] = i
        count += 1
        account -= 1
        cost = 1
    else:
        # print("Double")
        new_arr = [0] * (size * 2)
        for j in range(count):
            new_arr[j] = arr[j]
        account -= count
        arr = new_arr
        arr[count] = i
        size *= 2
        count += 1
        account -= 1
        cost = i
    
    print(i,"\t\t",size,'\t',cost,'\t\t3\t',account)