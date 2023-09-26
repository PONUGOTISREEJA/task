#even and odd numbers sep
list = [1,2,3,4,5,6,7,8,9,10]

even =[]
odd =[]
for j in list:
    if (j%2==0):
        even.append(j)
    else:
        odd.append(j)
print(even)
print(odd)

