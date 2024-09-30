# RaShun Lyons
# 9/30/2024
# Using imported library, math, and f-string
# P2LAB1

# Import math library
import math

# Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate diameter
diameter = 2 * radius

# Display diameter with one decimal place
print(f"The diameter of the circle is {diameter:.1f}\n")


# Calculate circumference
circum = 2 * math.pi * radius

# Display circumference with two decimal place
print(f"The circumference of the circle is {circum:.2f}\n")

# Calculate the area
area = math.pi * (radius ** 2)
area2 = math.pi * math.pow(radius, 2)

# Display area
print(f"The area of the circle is {area:.3f}")
