# Rashun Lyons
# 10/28/2024
# P4LAB1
# While loop to make square using turtle

# Import turtle library to use in code
import turtle

# Set up the window and Turtle object
window = turtle.Screen()
boss = turtle.Turtle()

boss.pensize(6)
boss.pencolor("purple")
boss.shape("arrow")

# While loop to draw 4 sides of square
line = 0
while line < 4:
    boss.right(90)
    boss.forward(150)
    line += 1

# For loop to draw triangle
for line1 in range(3):
    boss.left(120)
    boss.forward(150)
   
