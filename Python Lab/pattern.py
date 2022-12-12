# Pattern 1
n = 5
for i in range(n):
    print(" "*(n-i),end=' ')
    for k in range(i+1):
        print(chr(65 + k)+" ", end='')
    print()

# Pattern 2
m=5
for i in range(1,m+1):
    for j in range(0,i):
        print(m-i+j, end='')
    print()
for a in range(1,m+1):
    for b in range(0,m-a):
        print(b+a, end='')
    print()

# Pattern 3
m=5
for i in range(1,m+1):
    print(" "*(m-i),end=' ')
    for j in range(0,i):
        print(chr(65+m-i+j),end=' ')
    print()
for k in range(1,m):
    print(" "*k,end=' ')
    for l in range(0,m-k):
        print(chr(65+k+l),end=' ')
    print()