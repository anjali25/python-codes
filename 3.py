import math
import sys
n=int(sys.argv[1])
sum=0
for i in range(1,n):
   if (n%i==0):
     sum = sum +i
if (n==sum):
  print("Yes")
else:
    print("No")
