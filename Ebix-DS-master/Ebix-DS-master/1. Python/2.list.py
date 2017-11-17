#Basic List containers

list1 = [10,20,30]
print(type(list1))

list2 = ['abc', 10, True]
print(type(list2))

#access list elements by slicing
print(list1[0])
print(list1[1:2])
print(list1[2:3])

list1[2] = 100
print(list1)

list1.append(10)

list3 = [list1, 60, list2]
len(list3)
