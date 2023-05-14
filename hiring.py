import random
candidate=[0,1,2,3,4,5,6,7,8,9]
interview = []
hire = []
for i in range(0,10):
    x = random.choice(candidate)
    print(x)
    candidate.remove(x)
    interview.append(x)

# interview = [0,1,2,3,4,5,6,7,8,9] #worst case
# interview.reverse() #best case

print(interview)

for i,num in enumerate(interview,1):
    largest_num = max(interview[:i])
    hire.append(largest_num)

print(hire)

print("The number of candidates hired is : ",len(set(hire)))
cost = len(set(hire)) - 1
print("Thus firing cost will be : ", cost)
