#section teachr snd class 
c11=dict()
n=int(input('enter class '))
i=1
for i in range (n):
    s=input('enter section')
    t=input('enter name')
    c11[s]=t
    i=i+1
print('class',c11)
for i in c11:
    print("11","\t",i,"\t",c11[i])