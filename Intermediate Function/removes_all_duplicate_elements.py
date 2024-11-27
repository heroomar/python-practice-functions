def duplicate(r):
	return list(set(r))

_list = (input("Enter the list ex 1,2,3 : "))
_list = [int(i) for i in _list.split(',')]
print("after removing all duplicate elements: ",duplicate(_list))