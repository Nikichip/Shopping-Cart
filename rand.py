
r=print('your choices are given below')
a=print('A.to count the number of elements')
b=print('B.to read the elements in the list')
c=print('C.to find the sum')
d=print('D.to check whether element is present')
e=print('E.to divide even elemnts by2 and multiply odd by 2')
f=print('F.number divislible by other element and the sum')
g=print('G.delete all odd numbers')
h=print('H.create a 2d list')
i=print('I.read 2d list and display numbers divisible by 10')
j=print('J.sum of element is each row in nested list')
p=input("enter your choice : ")
if p==a:
    l=eval(input("enter number :"))
    c=0
    for i in l:
        c+=1
    print("the number is",c)
    

if p==b:
    l=eval(input("enter no"))
    for i in l :
        print(i,end=' ')
    
if p==c:
    l=eval(input("enter number"))
    s=0
    for i in l :
        s+=i
    print("the sum is ",s)
    
if p==d:
    l=eval (input("enter your number "))
    s=eval(input("enter elemnt to be found "))
    if s in l:
        print("number found")
    else:
        print("not found")
        
if p==f:
    n=int(input("enter n: "))
    p=int(input("element n: "))
    l= []
    for i in range(1,n+1):
        if i%p==0:
            l.append(i)
    print(l)
    print(sum(l))
            

        
            
    
