import sys
s1 = str(sys.argv[1])
s2 = s1[::-1]
print(str(s2))  
if (s1==s2):
  print('Palindrome')
else:
    print('Not a Palindrome')
