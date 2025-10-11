s=5
for i in range(1,s+1):
    print("  "*(s-i),end=" ")
    for j in range(i,1,-1):
        print(j,end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
         1 
       2 1 2 
     3 2 1 2 3 
   4 3 2 1 2 3 4 
 5 4 3 2 1 2 3 4 5 

n=int(input("enter the row : "))    
for i in range(1,n+1):
    print("  "*(n-i),end=" ")
    for j in range(1,i+1):
        print (j,end=" ")
    for j in range (j-1,0,-1):
        print(j,end=" ")       
    print()

         1 
       1 2 1 
     1 2 3 2 1 
   1 2 3 4 3 2 1 
 1 2 3 4 5 4 3 2 1
 
n=5
for i in range(n):
    for j in range(n,i,-1):
        print(j,end=" ")
    print()
    
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5
    
n=int(input("enter no "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1

s=int(input("enter  "))
for i in range(1,s):
    print(" "*(s-i),end=" ")
    print('*'*(2*i-1))
for i in range(s,0,-1):
    print(" "*(s-i),end=" ")
    print('*'*(2*i-1))
    
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *  
s=5
for i in range(1,s+1):
    print("  "*(s-i),end=" ")
    for j in range(i,1,-1):
        print(j,end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()  
for i in range(s-1,0,-1):
    print("  "*(s-i),end=" ")
    for j in range(i,1,-1):
        print(j,end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
         1 
       2 1 2 
     3 2 1 2 3 
   4 3 2 1 2 3 4 
 5 4 3 2 1 2 3 4 5 
   4 3 2 1 2 3 4 
     3 2 1 2 3 
       2 1 2 
         1 
    