def sum_even(list):
    total=0
    for num in list:
        if num % 2 == 0:
            total += num
    return total

list = (input("Enter the numbers list ex 1,2,3: "))
list = [int(i) for i in list.split(',')]
print("sum of all even numbers",sum_even(list))