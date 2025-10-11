s=int(input("enter  "))
for i in range(1,s):
    print(" "*(s-i),end=" ")
    print('*'*(2*i-1))
for i in range(s,0,-1):
    print(" "*(s-i),end=" ")
    print('*'*(2*i-1))
    
s=5

for i in range(s-1,0,-1):
    print("  "*(s-i),end=" ")
    for j in range(i,1,-1):
        print(j,end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()  





s=5
for i in range(1,s+1):
    print("  "*(s-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(j-1,0,-1):
        print(j,end=" ")
    print()

