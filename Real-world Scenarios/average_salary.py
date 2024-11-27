def average_salary(salaries) -> int:
    if len(salaries) == 0:
        return 0  # Return 0 if the list is empty to avoid division by zero
    return sum(salaries) / len(salaries)


salaries = [50000, 60000, 75000, 55000, 80000]
print("Average salary:", average_salary(salaries))
