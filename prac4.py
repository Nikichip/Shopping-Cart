n=5
i=[0,1,2,3,4,5,6]
for i in range(0,n+1):
    print(' #'*(2+i-1))
#
# #
# # #
# # # #

for i in range (1,n+1):
    print(" "*(n-i),end=" ")
    print('*'*(2*i-1))

       #
     # # #
   # # # # #
 # # # # # # #

for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    print('#'*(2*i-1))
    
# # # # # # # # #
  # # # # # # #
    # # # # #
      # # #
        #

for i in range (0,n):
    print(' #'*(n-i))
    
 # # # # #
 # # # #
 # # #
 # #
 #
    