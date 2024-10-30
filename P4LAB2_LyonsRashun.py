# RaShun Lyons
# 10/30/2024
# P4LAB2
# Use a for loop and a while loop to display positive multiplication tables

# Create variable to make program run first time
run_again = "yes"

# While loop to control entire program
while run_again == "yes":
    print()

    # Get input from user
    userNum = int(input("Enter an integer: "))
    print()
    
    # Check if userNum is positive
    if userNum >= 0:
        # Loop to print multiplication
        for num in range(1,13):
            print(f"{userNum} * {num} = {userNum*num}")
        print()
            
    # If userNum is negative, tell the user
    else:
        print("Program does not handle negative numbers")

    print()        
    run_again = input("Would you like to run the program again (yes/no)? ").lower()

# Loop breaks
print("Exiting program...")
