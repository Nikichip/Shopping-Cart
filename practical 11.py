n=int(input("enter number:"))
for i in range(1,n+1):
    for j in range(2,n):
       if i % j==0:
           break
       else:
           print(i)
            