import math
import sys
s = str(sys.argv[1])
n = int(sys.argv[2])
count=0
length = len(s)
if " " in s:
   length = length - s.count(" ")
while count == 0:
      if (n <= length):
        words= length - n
        def factorial(n):
           if n == 0:
              return 1
           else:
                return n * factorial(n-1)
        total= factorial(length)
        nletter= factorial(words)
        per = total/nletter
        print (int(per))
        count = count - 1
        break

      else:
           print "Length of ", s ,"is smaller than", n,".Enter n again:",
           n = input()

 
