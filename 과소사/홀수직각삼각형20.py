n = int(input())
c = 1
for i in range(n):
    for j in range(i+1):
        print(c, end=" ")
        c+=2
    print()