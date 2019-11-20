def rearrange(a):
 b= []
 y = c = len(a)-1
 for i in range(len(a)):
  if len(b) < (y+1):
   b.append(a[c])
  if(i < c):
   b.append(a[i])
   c = c-1
  else:
   break
 return b

list_a = [1,2,3,4,5,6,7]
print "Input value is: ", list_a
print "Result is: ", rearrange(list_a)
