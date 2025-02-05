import copy
list1=[1,[2,3],4]
list3=list.copy()
list3=copy.deepcopy(list1)

list1[0]=10
list1[1][0] = 20 
print("list1:", list1)
print("list2:", list2) 
print("list3:", list3) 
