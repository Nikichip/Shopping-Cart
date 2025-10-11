x=eval(input("Enter a x:"))
n=int(input("Enter a n:"))
su,sign=1,-1
for i in range(2,n+1):
    f=1
    for j in range(1,2*i):
        f*=j
    su+=sign*( x**(2*i-1)/f)
    sign*=-1
print("Sum of series:",su)