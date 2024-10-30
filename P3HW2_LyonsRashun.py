# RaShun Lyons
# 10/28/2024
# P3HW2
# Calculate the gross pay for employee based on hours worked, pay rate and overtime

# Get employee details
employee_name = input("Enter the name of the employee: ")
hours_worked = float(input("Enter the number of hours worked this week: "))
pay_rate = float(input("Enter the employee's pay rate: "))

# Variables
if hours_worked > 40:
    overtime_hours = hours_worked -40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Calculate pay
overtime_pay = overtime_hours * (pay_rate * 1.5)
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Display results
print("Employee Name: ", employee_name)
print("Pay Rate: $", pay_rate)
print("Hours Worked:", hours_worked)
print("Overtime Hours:", overtime_hours)
print("Overtime Pay: $", round(overtime_pay, 2))
print("Pay for Regular Hours: $", round(regular_pay, 2))
print("Gross Pay: $", round(gross_pay, 2))

      
