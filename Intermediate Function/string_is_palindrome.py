def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

str = (input("Enter the string: "))

if palindrome(str):
    print("The string is a palindrome")
else:
    print("The string is not palindrome")