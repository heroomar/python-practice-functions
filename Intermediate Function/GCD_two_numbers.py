def gdc(num1,num2):
    while num2 !=0:
        print(num1 , num2,num1 % num2)
        num1,num2=num2,num1 % num2
        # print(num1,num2)
    return num1


num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))


print("GCD (Greatest Common Divisor) of two numbers is:",gdc(num1, num2))