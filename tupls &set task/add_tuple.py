# tuple = ("apple","banana","cherry")
# tuples = list(tuple)
# print(tuples)
# tuples.insert(2,"kiwi")
# print(tuples)
d = {}
q = ""
while True:

 

 if q=="q":
  break
 else:
  key, value = input("enter key and value like key-value").split("-")
  d[key] = value
 q = input("if you want add items press y, to quit press q")

print(d)