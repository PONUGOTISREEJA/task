str1 = input("enter a string: ")
total = 0
for i in str1:
    if i.isdigit():
        total += int(i)
print("sum of digits in string ",total)
