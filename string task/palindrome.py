def ispalindrome(s):
    return s == s[::-1]
s = "anana"
# print(str[::-1])
ans = ispalindrome(s)
if ans:
  print("palindrome")  
else:
  print("Not palindrome")  

