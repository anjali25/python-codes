s = raw_input("Enter list: ")
s = s.split()
length = len(s)
diction = {}
for i in range(0,length-1,2):
	diction.update({s[i]:int(s[i+1])})
print diction
