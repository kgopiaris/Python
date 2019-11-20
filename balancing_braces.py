def balancing_braces(input):
 b = {}
 d =[]
 for i in range(len(input)):
  b[i]=input[i]
 for key, val in b.items():
  if val == "(":
   d.append(key)
  elif val == ")":
   d.pop()
 
 for itm in d:
  del b[itm]
 str = ''
 for key, val in b.items():
  str = str + b[key]
 return str

input = "(((a)(b))"
output = balancing_braces(input)
print "Input: ", input, "\nOutput: ", output
