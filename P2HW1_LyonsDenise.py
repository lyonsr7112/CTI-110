# RaShun Lyons
# 9/23/2024
# P1HW2
# Figure travel budget and expenses

print("This program calculates and displays travel expenses ")
print()

# Get budget amount
budget = int(input ("Enter Budget: $"))
print()

# Get travel destination
city = input("Enter your travel destination: ")
print()

# Get how much will be spent on gas
gas = int(input("How much do you think you will spend on gas? $"))
print()

# Get approximate amount needed for hotel accomodation
hotel = int(input("Approximately, how much will you need for accomodation/hotel? $"))
print()

# Get amount needed for food
food = int(input("Last, how much do you need for food? $"))
print()
print()

print("----------Travel Expenses----------")
#Subtract travel expenses from budget
print(f"{'Location':<18}{city:<25}")
print(f"{'Initial Budget':<18}${budget:<25,.2f}")
print(f"{'Fuel':<18}${gas:<25.2f}")
print(f"{'Accomodation':<18}${hotel:<25.2f}")
print(f"{'Food':<18}${food:<25.2f}")
print("-" * 30)
total = budget-gas-hotel-food
print()
print(f"{'Remaining Balance':<18}${total:<25.2f}")

