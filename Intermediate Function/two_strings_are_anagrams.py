def anagram(a,b):
    return sorted(a.lower()) == sorted(b.lower())

str1 = (input("Enter string 1: "))
str2 = (input("Enter string 2: "))

if anagram(str1,str2):

    print("the given string are anagram ")
else :
    print("the given string are not anagram ")