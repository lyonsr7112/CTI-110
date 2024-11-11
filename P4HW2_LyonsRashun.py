# RaShun Lyons
# 11/9/2024
# P4HW2
# Calculate the gross pay for employee based on hours worked, pay rate and overtime

# Get employee details
employee_name = input("Enter employee's name or 'Done' to terminate: ")
hours_worked = float(input("How many hours did Nancy Drew work? "))
pay_rate = float(input("What is Nancy Drew's pay rate? "))

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
print("Hours Worked:", hours_worked)
print(f"Pay Rate: ${pay_rate:.2f}")
print("Overtime Hours:", overtime_hours)
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Pay for Regular Hours: ${regular_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")
