str1 =input("enter string: ")
digit_total=0
alphabet_total =0
special_total=0
for i in str1: 
 if i.isalnum():
    if i.isdigit():
        digit_total = digit_total + 1
    else:
        alphabet_total = alphabet_total + 1
 else:
    special_total = special_total + 1
print(f"number of special charaters {special_total}\nnumber of digits {digit_total}\nnumber of alphabets {alphabet_total}")