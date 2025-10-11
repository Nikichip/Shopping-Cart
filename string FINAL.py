#TO CHECK Plindrome or not(same reading backward)
#s=input("enter string")
#if s==s[ ::-1]:
#    print(s,"palindrome")
#else:
#    print("not")
###################################################################
 
#count no of letter and numbers
#s=input("enter string")
#l=0
#n=0
#for i in s:
#    if i.isalpha():
#        l+=1
#    elif i.isdigit():
#        n+=1
#print("the digita r ",n)
#print("the alpha r ",l)
###################################################################

#altrenate character printing
#s=input("enter string ")
#for i in range(0,len(s),2):
#    print(s[i],end=" ")
###################################################################

#replace punctuation marks with space
#s=input("enter string")
#s1=" "
#for i in range(0,len(s)):
#    if not s[i].isalnum():
#        s1+=" "
#    else:
#        s1+=s[i]
#                  print(s)
###################################################################

#count the no of substring in string

#s=input('enetr string')
#s1=input('enter substring')
#print(s1,s.count(s1))       

#c=0
#for i in s.split():
#    if i == s1:
#        c+=1
#print(s1,c)
###################################################################

#capitalize first letter
#s=input("enter string")
#print(s.title())
###################################################################

#lower case to uppercase and vice versa
#s=input("enter string ")
#s1=" "
#for i in range(0,len(s)):
#    s1+=s[i].lower()
#    if i<len(s)-1:
#        s1+=s[i+1].upper()
#print(s)
###################################################################

#s=input("enter id")
#if s.endswith("@gemsedu.com"):
#    print("valid")
#else:
#    print("invalid")
###################################################################

#pattern with name
#s=input("enter name")
#for i in range(1,len(s)+1):
#    print(s[1],end=" ")
#print()
#wrong#############################################################

#longest word
#s=input("enter word")
#long=' '
#for i in s.split():
#    if len(i)>len(long):
#        long=i
#print(long)
###################################################################

#longest string in constants
#s=input("enter string ")
#long=' '
#for i in s.split():
#    for j in i:
#        if j in i:
#            if j in 'aeiouAEIOU':
#                break
#            else:
#                if len(i)>len(long):
#                    long=i
#print(long)
                     