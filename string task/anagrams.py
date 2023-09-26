str1 = input("enter a firststring: ")
str2 = input("enter a secoundstring: ")
if len(str1) != len(str2):
    print("The given strings are not Anagrams.")
else:
    if sorted(str1) == sorted(str2):
        print("The given strings are Anagrams.")
