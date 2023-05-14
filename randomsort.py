import random
import time
c1, c2 = 0, 0

def quicksort(arr):
    global c1
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        c1 += len(left) + len(right)
        return quicksort(left) + [pivot] + quicksort(right)

def random_quicksort(arr):
    global c2
    if(len(arr) <= 1):
        return arr
    
    pivot = random.choice(arr)
    left = []
    equal = []
    right = []

    for i in arr:
        if(i < pivot):
            left.append(i)
            c2 += 1
        elif(i == pivot):
            equal.append(i)
            c2 += 1
        else:
            right.append(i)

    return quicksort(left) + equal + quicksort(right)

arr = [3,7,22,32,4,51,34,11,56,86,9,87]
arr1 = arr.copy()
print('Input Array : ', arr)

print("\n---------Quick Sort------------")
start = time.time()
sorted_arr = quicksort(arr)
end = time.time()
print('Output Array: ', sorted_arr)
print('Time for normal quick sort: ', end-start)
print("Number of comparisions in normal quick sort :", c1)

print("\n---------Randomised Quick Sort------------")
start_rqs = time.time()
sorted_arr_rqs = random_quicksort(arr1)
end_rqs = time.time()
print('\nOutput Array: ', sorted_arr_rqs)
print('Time for randomised quick sort: ', end_rqs-start_rqs)
print("Number of comparisions in randomized quick sort :", c2)