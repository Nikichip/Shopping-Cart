
print('your choices are given below')
print('A.to count the number of elements')
print('B.to read the elements in the list')
print('C.to find the sum')
print('D.to check whether element is present')
print('E.to divide even elemnts by2 and multiply odd by 2')
print('F.number divislible by other element and the sum')
print('G.delete all odd numbers')
print('H.create a 2d list')
print('I.read 2d list and display numbers divisible by 10')
while True:
    p=input("enter your choice : ")
    if p==a:
        l=eval(input("enter number :"))
        c=0
        for i in l:
             c+=1
        print("the number is",c)
    elif p==b:
        l=eval(input("enter no"))
        for i in l :
             print(i,end=' ')
    elif p==c:
        l=eval(input("enter number"))
        s=0
        for i in l :
             s+=i
        print("the sum is ",s)
    elif p==d:
         l=eval (input("enter your number "))
         s=eval(input("enter elemnt to be found "))
         if s in l:
             print("number found")
         else:
             print("not found")
        
    elif p==f:
         n=int(input("enter n: "))
         p=int(input("element n: "))
         l= []
         for i in range(1,n+1):
                     if i%p==0:
                       l.append(i)
         print(l)
         print(sum(l))
            

        
            
    
