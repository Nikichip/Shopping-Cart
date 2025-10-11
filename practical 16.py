print("menu")
print("1.append an element")
print("2.insert an element")
print("3.append a list to the given list")
print("4.modify an existing element")
print("5.delete an existing element from its position")
print("6.sort the list in ascending order")
print("7.sort the list in descending  order")
print("8.search for a given number in the list")
print("9.find sum average maximum and minimum of elements in the list")
print("10.to swap element at the even location with th elements in th eodd location.")
print("11.display only the even element from the list")
print("12.display elements at the odd locations in the list")
n=int(input("enter the step to be done: "))
l=eval(input('enter list: '))
if n==1:
    a=eval(input("enter element to append: "))
    l.append(a)
    print("new list",l)
elif n==2 :
    b=eval(input("enter element to insert: "))
    b2=int(input("enter the index: "))
    l.insert(b2,b)
    print("new list",l)
elif n==3 :
    c=eval(input("enter new list : "))
    l.append(c)
    print("list",l)
elif n==4 :
    d=eval(input("enter elment :"))
    d2=int(input("enter index :"))
    l[d2]=d
    print("list",l)
elif n==5:
    e=eval(input("enter element: "))
    l.remove(e)
    print("list",l)
elif n==6 :
    l.sort()
    print("list",l)
elif n==7 :
    l.sort(reverse= True)
    print("list :",l)
elif n==8 :
    f=eval(input("enter number :"))
    for i in range (len(l)):
        if l[i]==f:
            print("the number is present ")
elif n==9 :
    print("the sum is ",sum(l))
    print("the average is ",sum(l)/len(l))
    print("the minimum number is ",min(l))
    print("the maximum number is ",max(l))
elif n==10 :
    for i in range (0,len(l)-1,2):
        l[i],l[i+1]=l[i+1],l[i]
    print(l)
elif n==11 :
    for i in len(l):
        if l[i]%2==0:
            print(i,end=" ")
elif n==12 :
    for i in l:
        if i%2 !=0:
            print(i,end=" ")
            

    