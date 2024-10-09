# RaShun Lyons
# 10/9/2024
# P2HW2
# Figure grades and grade averages from list

# Enter grades for each module

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))
print()
print()
print("---------------Results---------------")
# Grades for each module
grades = [module1, module2, module3, module4, module5, module6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average = sum(grades) / len(grades)
print(f"{'Lowest Grade:':<15} {lowest_grade}")
print(f"{'Highest Grade:':<15} {highest_grade}")
print(f"{'Sum of Grades:':<15} {sum_of_grades}")
print(f"{'Average:':<15} {average:.2f}")
print("-------------------------------------")      


                
