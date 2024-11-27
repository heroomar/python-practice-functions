def count_vowels(str):
    count=0
    char = 'aeiouAEIOU'
    for c in str:
        if c in char:
            count+=1
    return count
str = int(input("Enter str here: "))

print("The vowels in the given string are :",count_vowels(str))