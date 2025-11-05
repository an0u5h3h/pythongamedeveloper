list1=["january","february","march","april","may","june"]
print(list1[3])
list1.append("august")
list1.insert(6,"july")
print(list1)
list2=["september","october","november","december"]
list2.remove("november")
print(list2)
print(list1.index('may'))
print(list2.index('december'))
print(len(list1))
print(len(list2))

if "october" in list2:
    print("yes")
else:
    print("no")

if "november" in list1:
    print("yes")
else:
    print("no")