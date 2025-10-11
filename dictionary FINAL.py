#dict={}
#dict['name']='ria'
#dict['age']=30
#print(dict)

#section teachr snd class 
#c11=dict()
#n=int(input('enter class '))
#i=1
#for i in range (n):
#    s=input('enter section')
#    t=input('enter name')
#    c11[s]=t
#print('class',' section ',' teach ')
#for i in c11:
#    print("11","\t",i,"\t",c11[i])
#############################################################################

#phone=dict()
#n=int(input('enter frnds '))
#for i in range (n):
#    s=input("enter name")
#    t=int(input('enter number'))
#    phone[s]=t
#print(phone)
#for i in phone:
#    print(i,'-',phone[i])
#############################################################################

#to count the number of frequency of words
#t=input("enter sentence ")
#l=t.split()
#d={}
#for i in l:
#    if i.lower()not in d:
#        d[i.lower()]=1
#    else:
#        d[i.lower()]+=1
#print('frequency of words is',t)
#for i in d:
#    print(i,':',d[i])
#############################################################################

#to delete a friend
#phone=dict()
#n=int(input('enter frnds '))
#for i in range (n):
#    s=input("enter name")
#    t=int(input('enter number'))
#    phone[s]=t
#f=input("enter frnd name to dlt")
#print(phone.pop(f,'name not found'))
#for i in phone:
#    print(i,'-',phone[i])
############################################################################

#employ list
#emp=dict()
#n=int(input('enter emp how many ? ' ))
#for i in range (n):
#    s=input("enter name")
#    t=int(input('enter number'))
#    emp[s]=t
#    l=list(emp.keys())
#    l.sort()
#print("emp name","\t","emp number",)
#for i in l:
#    print(i,"\t""\t""\t",emp[i])
############################################################################

#
#phone=dict()
#n=int(input('enter frnds '))
#for i in range (n):
#    s=input("enter name")
#    t=int(input('enter number'))
#    phone[s]=t
#print(phone)
#    l=sorted(phone.values())
#print(l)
#a=input("entet name ")
#b=int(input("number "))
#phone[a]=b
#print(phone)
#s=input("frnd name modify")
#t=int(input("modified num "))
#phone[s]=t
#print(phone)
#############################################################################

# d1 has same keys as d2
#d1=eval(input("enter "))
#d2=eval(input("enter "))
#l=[]
#for i in d1:
#    if i in d2:
#        l.append(i)
#print(l)
 ############################################################################  

#
l={}
x={'k1':'v1','k2':'v2','k3':'v3'}
for i in x:
    x[i]=i
print(x)



#############################################################################