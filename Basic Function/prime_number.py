def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num+1, 2):
        # print(i)
        if num % i == 0 and num != i:
            return False
    return True
num = int(input("Enter num here: "))

if is_prime(num):
    print(f"The given number is prime")
else:
    print(f"The given number is not prime")
