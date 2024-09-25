# RaShun Lyons
# 9/23/2024
# P1HW2
# Figure travel budget and expenses

print("This program calculates and displays travel expenses ")
print()

# Get budget amount
budget = int(input ("Enter Budget: $"))

# Get travel destination
city = input("Enter your travel destination: ")

# Get how much will be spent on gas
gas = int(input("How much do you think you will spend on gas? $"))

# Get approximate amount needed for hotel accomodation
hotel = int(input("Approximately, how much will you need for accomodation/hotel? $"))

# Get amount needed for food
food = int(input("Last, how much do you need for food? $"))
print()
print()
print("----------Travel Expenses----------")

#Subtract travel expenses from budget
print("Location: ", city)

print("Initial Budget: $",budget)
print()

print("Fuel: $", gas)
print("Accomodation: $", hotel)
print("Food: $", food)
print()

total = budget-gas-hotel-food

print("Remaining Balance: $", total )

