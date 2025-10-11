s=input("enter string ")
sum = 0
for i in s:
    if (i.isdigit()):
        sum+=int(i) 
print("the sum is ",sum)

#enter string 12ioh3
#the sum is  6

n=input("enter inoput ")
a='aeiou'
c=0
for i in n:
    if i in a:
        c=c+1
print("The number of vowels is",c)

#enter inoput today is a pleasent day
#The number of vowels is 13

x=int(input("enter string"))
n=int(input("enter number"))
sum=1
sign=-1
for i in range(2,n+1):
    f=1
    for j in range(i,2*i):
        f*=j
    sum+=sign*(x**(2*i-1)/f)
    sign*=-1
print("sum= ",sum)

#(x)=n**x/n!

i=1
while (i<=10):
    print('i= ',i)
    i+=2
    
#i=  1
#i=  3
#i=  5
#i=  7
#i=  9
    
for i in range(20,0,-2):
    print('i= ',i)
    
#i=  20
#i=  18
#i=  16
#i=  14


