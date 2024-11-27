def pon(num,power):
    out=1
    for i in range(power):
        out *= num
    return out
num = int(input("Enter number: "))
power = int(input("Enter the power: "))

print("power of a number is :",pon(num,power))