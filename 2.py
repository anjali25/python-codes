
import sys
import math
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])
perimeter=int(a+b+c)
per=(a+b+c)
s=per/2.0
area=int(math.sqrt(s*(s-a)*(s-b)*(s-c)))
print (str(perimeter)+'\n'+str(area))

