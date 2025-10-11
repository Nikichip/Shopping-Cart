#n=int(input('enter '))
n=5
for i in range(1,n+1):
    p=1
    for j in range(1,n+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
        p+=1
    for i in range (1,n+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
        p-=1
    print()

     