def largest_num(r):
	return max(r)

list = (input("Enter the numbers ex 1,2,3 : "))
list = [int(i) for i in list.split(',')]
print("The largest number list is: ",largest_num(list))