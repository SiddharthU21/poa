def multipop(st, ele):
    print(st)
    for i in range(ele):
        if len(st) == 0:
            print("cannot pop element as stack is empty")
        else :
            print("Popped:", st.pop())

n = int(input("Enter number of elements: "))

print("Enter all", n, "elements: ")
v = []
for i in range(n):
    v.append(int(input()))

count = 0
st = []

for i in range(n):
    siz = len(st) + 1

    if v[i] <= siz:
        multipop(st, v[i])
        count += v[i]

    count += 1
    print("Pushed :", v[i])
    st.append(v[i])

print("Total cost:", count)
print("Therefore cost of operation is T(n)/n:", count/n)

print(st)


# dynamic Table

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

size = 1
count = 0
arr = [0] * size
p = arr
total_cost = 0
num_operations = 0  # keep track of total number of operations

while True:
    n = int(input("Enter the number you wish to insert in the dynamic table: "))
    if n == -1:
        break
    if count < size:
        p[count] = n
        count += 1
        print(p)
        print_array(p[:count])
        total_cost += 1
    else:
        # double array
        print("Double")
        new_arr = [0] * (size * 2)
        for i in range(count):
            new_arr[i] = p[i]
        total_cost += count + 1
        size *= 2
        new_arr[count] = n
        count += 1
        p = new_arr
        print(p)
        print_array(p[:count])
    num_operations += 1  # increment total number of operations
    print("Total amortized cost :", total_cost)
    amortized_cost = total_cost / num_operations  # calculate amortized cost
    print("Amortized cost per operation :", amortized_cost)
    print()
