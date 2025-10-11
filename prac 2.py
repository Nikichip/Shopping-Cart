n=int(input("enter "))
for i in range(0,n+1):
    print("  "*(n-i),end=" ")
    for j in range(i,1,-1):
        print(j,end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
     
     
#             1 
#           2 1 2
#          3 2 1 2 3 
#       4 3 2 1 2 3 4 
#     5 4 3 2 1 2 3 4 5 