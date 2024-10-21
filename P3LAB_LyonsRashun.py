# RaShun Lyons
# 10/14/2024
# P3LAB
# Calculate most efficient coin combination
'''
# Regular Division
print(100/3)

# Floor Division - returns integer portion of quotient
print(100//3)

# Modulo - returns ONLY the remainder
print(100%3)
print(7%4)
'''

# Get amount of money from user as a float
money = float(input("Enter the amount of money as a float: $"))

# Convert money to a whole number
money = round(money * 100)

# May need to round this value
#money = round(money * 100)
#print(money)

# Get whole dollars from money amount
dollars = money // 100
print(f"Dollars:{dollars}")

# Remove the dollar amount from money
money = money - (dollars * 100)

# Get quarters from money amount
quarters = money // 25
print(f"Quarters:{quarters}")

# Remove the quarters amount from money
money = money - (quarters * 100)
    
# Get dimes from money amount
dimes = money // 10
print(f"Dimes:{dimes}")

# Remove the dimes amount from money
money = money - (dimes * 100)

# Get nickles from money amount
nickles = money // 5
print(f"Nickles:{nickles}")

# Remove the nickles amount from money
money = money - (nickles * 100)

# Get pennies from money amount
pennies = money
print(f"Pennies:{pennies}")

# Remove the pennies amount from money
money = money - (pennies * 100)

                
