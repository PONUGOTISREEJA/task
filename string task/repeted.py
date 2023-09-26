string =input("enter a string ")

res=""
for char  in string:
    if char not in res:
        res = res+char
print(res)