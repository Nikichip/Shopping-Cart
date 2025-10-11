#t=tuple()
#print("subject names below")
#for i in range(5):
#    a=input("enter your name ")
#    t=t+(a,)
#print('the tuple is ',t)

#l=eval(input("number"))
#f=eval(input("numb"))
#print(l)
#print(f)
#l,f=f,l
#print("after swapping")
#print(l)
#print(f)
################################################################################################

#for i in range(3):
#    n=int(input("enter number"))
#    t=t+(n,)
#print(t)
#print(max(t))
#print(min(t))
################################################################################################
 
#n=eval(input("enter "))
#l=eval(input("number "))
#for i in range (len(n)):
#    if n[i]==l:
#        print("found",i)
#        break
#else:
#    print("invalid")
################################################################################################        

#n=eval(input("tuple  "))
#for i in n:
#    if i not in t:
#        print('frequency',i,'is',n.count(i))
#        t+=(i,)
################################################################################################

#n=eval(input("enter "))
#print("mean ,",sum(n)//len(n))
################################################################################################

#TO PRINT X,X^2,X^3,X^4
#for i in range(5):
#    n=eval(input("enter "))
#    a=n**2
#    b=n**3
#    c=n**4
#    t=t+(n,a,b,c)
#print(t)

#altrenate way

#for i in range(5):
#    n=eval(input("enter "))
#    for j in range(1,5):
#        t+=(n**j,)
#print(t)
###############################################################################################

#m=()
#t=()
#a=()
#for i in range (3):
#    m1=eval(input("enter marks 1 :"))
#    m2=eval(input("enter marks 2 :"))
#    m3=eval(input("enter marks 3 :"))
#    s=(m1,m2,m3)
#    m=(s)
#    t=(sum(s))
#    a=(sum(s)//3)
#    print("marks is",m)
#    print("total is",t)
#    print("average is",a)
##############################################################################################

#t=eval(input("enter "))
#m=max(t)
#secmax=t[0]
#for i in range(len(t)):
#    if m>t[i]>secmax:
#        secmax=t[i]
#print(secmax)
#############################################################################################

#CHECK ELEMENTS IN BOTH
#t=eval(input("enter "))
#t2=eval(input("enter "))
#for i in t:
#    if i not in t2:
#        print("false")
#        break
#else:
#    print("trues")
#############################################################################################

#FIBANNACI SERIES TUPLE
#n=9
#f=[]
#a,b=0,1
#for i in range (n-1):
#    a,b=b,a+b
#    f.append(a)
#print(f)
##############################################################################################

#integers raise to their numbers
#t=tuple()
#for i in range(1,51):
#    t+=(i**i,)
#print(t)

#for i in range(1,51):
#    t+=(i**2,)
#print(t)
##############################################################################################

#('a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg', 'hhhhhhhh',.....)
#t=tuple()
#n=1
#for i in range(ord('a'),ord('z')+1):
#    t+=(chr(i)*n,)
#    n=n+1
#print(t)
##############################################################################################

#mean of nested loop

