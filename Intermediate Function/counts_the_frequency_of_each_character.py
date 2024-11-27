def count_char(str):
	str = str.replace(' ','').lower()
	conunts = [0]*26
	for c in str:
		if ord(c)-97 >= 0:
			conunts[ord(c)-97] += 1
	for i in range(len(conunts)):
		if conunts[i] > 0:
			print(chr(i+97),' => ',conunts[i])

str = (input("Enter the string : "))
# str = 'a function that takes a string and counts the frequency of each character'
print("The largest number list is: ",count_char(str))