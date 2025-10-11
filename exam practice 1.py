#i=2
#n=int(input('enter '))
#while i<n:
#    if n%i==0:
#        break
#    print(i)
#    i=i+1
#else:
#    print('donr')
#----------------------------------------------

#keepgoing=True
#x=100
#while keepgoing:
#    print(x)
#    x=x-10
#    if x<50:
#        keepgoing=False
#---------------------------------------------

x=int(input('enter '))
for i in range(0,10):
    if x==i:
        print(x+i)
    else:
        print(x-i)