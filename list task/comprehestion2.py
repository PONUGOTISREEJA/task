list1 = [1,3,5,66,88]
list2 = [90,100]
a = 0 
for  i in list2:
    if i in list1:
        a = 1 
if a == 1:
    print("True")
else:
    print("False")