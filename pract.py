L1=eval(input("enter list:"))
a={}
for i in L1:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
print("frequesncy of the elements of the list is:", str(a))


