str=input("enter sentence:")
x=""
y=str.split()
for i in y:
    x+=i.capitalize()+ " "
print("string:",x)