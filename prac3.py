n=int(input('enter '))
k=5
for i in range(1,n+1):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n+1):
        print(j,end=" ")
    print()


