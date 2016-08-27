l = raw_input("Enter list: ")
l = l.split(',')
count=0
length = len(l)
for i in range (length-1,0,-1):
   for j in range(0,i):
      if (l[j] > l[j+1]):
	l[j], l[j+1] = l[j+1], l[j]
      count = count+1
      string = ','.join(l)      
      print "Exchange ",count,":",string
print "Sorted list:",string

