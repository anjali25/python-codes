
import sys
n=int(sys.argv[1])
s1=""
for i in range(1,(n+1)):
   if (i!=n):
     print " "*((n-1)-i),
     for j in range(1,(i+1)): 
        s1=s1+str(j)
     for k in range((i-1),0,-1):
        s1=s1+str(k)
     print(str(s1))
     s1="" 
   else:
       for j in range(1,(i+1)): 
          s1=s1+str(j)
       for k in range((i-1),0,-1):
          s1=s1+str(k)
       print(str(s1))
       s1=""
   
