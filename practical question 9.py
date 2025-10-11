L=eval(input("enter list:"))
s=0
for i in L:
    s+=i
    a=s//len(L)
print(s,"sum<   >average",a)
print("largest element is:",max(L))
print("smallest element is:",min(L))