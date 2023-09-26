list1 = [1,2,3,4,5]
list2 = [1,2,6,7,8]
lst = any (check in list1 for check in list2)
if lst:
    print("True")
else:
    print("False")

