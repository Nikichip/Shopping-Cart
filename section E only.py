s=input('enter string')
print(s.swapcase())

# can be done both ways

s=input('enter string')
if s.isupper():
    print(s.lower(),end=" ")
elif s.islower():
    print(s.upper(),end=" ")
else:
    print("no string to convert")
print()
    
s=input("ener string ")
print(s.title(),end=" ")