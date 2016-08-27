import sys
import math
l= str(sys.argv[1])

if (len(sys.argv) == 3):
  word= str(sys.argv[2])
else:
  word= ''

ls = l.split(',')
length = len(ls)
def evenSum(ls):
   s_even=0
   for i in range(length):
      if (int(ls[i])%2 == 0):
         s_even = s_even+int(ls[i])
   return s_even
def oddSum(ls):
   s_odd=0
   for i in range(length):
      if (int(ls[i])%2 != 0):
         s_odd = s_odd+int(ls[i]) 
   return s_odd
if (word == "even" or word == "EVEN" or word == "Even"):
  print evenSum(ls)
else:
  print oddSum(ls)

