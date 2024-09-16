# RaShun Lyons
# 9/16/2024
# P1HW1
# Using math expressions with user input

print("--------Calculating Exponents--------")

base_value = input("Enter an integer as the base value: ")

# Convert base_value to integer
base_value = int(base_value)

# Get input from user and convert to integer
exponent = int(input("Enter an integer as the exponent: "))

# Display math result to the user
print(base_value, "raised to the power of", exponent, "is", base_value**exponent)

