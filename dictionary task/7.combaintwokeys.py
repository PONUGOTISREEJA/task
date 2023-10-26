dict1 = {'a':100,'b':200,'c':300}
dict2 = {'a':300,'b':200,'d':400}
dict = dict2
for i ,j in dict1.items():
    if i in dict2:
        dict[i] = j + dict2[i]
    else:
        dict[i] = j
print(dict)