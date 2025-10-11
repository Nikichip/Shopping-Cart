n=int(input("enter no:"))
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print(" ")
    
for i in range(1, n):
    num = 1
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")
    