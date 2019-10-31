""" Print the combinaions of 3 digit number """
n = input("Enter the value\n")
a = [int(i) for i in str(n)]
for i in range(len(a)):
  for j in range(len(a)):
    for k in range(len(a)):
      if i !=j and j != k and k != i:
        print str(a[i])+str(a[j])+str(a[k])
