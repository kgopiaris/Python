# Excercise Problems and solutions using Python

> #### Problem 1:
##### The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

```sh 
Input          Output
-----          ------
"din"      =>  "(((" 
"recede"   =>  "()()()" 
"Success"  =>  ")())())" 
"(( @"     =>  "))((" 

```

> #### Solution:
```sh
def duplicate_encode(word):
 chars_dict = {}
 str1 = ''
 for i in word.lower():
  chars_dict[i] = chars_dict[i] +1 if chars_dict.get(i) else 1
 print chars_dict
 for i in word.lower():
  if chars_dict[i] == 1:
   str1 += "("
  else:
   str1 += ")"
 print word, " => ", str1

word= "recede" 
duplicate_encode(word)
```
