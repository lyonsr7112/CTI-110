# RaShun Lyons
# 11/4/2024
# P4HW1
# Collect the number of scores and determine the letter grade

# Ask the user for the number of scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Initialize a list to store valid scores
score_list = []

# Loop to collect valid scores
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i + 1}: "))
            # Validate the score
            if 0 <= score <= 100:
                score_list.append(score)
                break # Exit the inner loop if the score is valid
            else:
                print("INVALID Score entered!!!! ")
                print("Score should be between 0 and 100. ")
        except ValueError:
            print("Invalid input. Please enter a numeric value. ")

# Calculate statistics for the valid scores
lowest_score = min(score_list)
modified_scores = [score for score in score_list if score != lowest_score]

if modified_scores: # Check to avoid division by zero
    average_score = sum(modified_scores) / len(modified_scores)
else:
    average_score = 0 # Handle case where all scores are the same

# Determine the letter grade based on the average score
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display the results
print("\n-------------Results----------- ")
print(f"Lowest score: {lowest_score}")
print(f"Modified list: {modified_scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade: {letter_grade}")
print("------------------------------- ")









