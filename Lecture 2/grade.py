# Ask the user for their score and convert it to an integer
score = int(input("Score: "))

# Check the range of the score and assign a grade accordingly
if score >= 90 and score <=100:
    # If the score is between 90 and 100, the grade is A
    print("Grade: A")
elif score >= 80 and score < 90:
    # If the score is between 80 and 89, the grade is B
    print("Grade: B")
elif score >= 70 and score < 80:
    # If the score is between 70 and 79, the grade is C
    print("Grade: C")
elif score >= 60 and score <70:
    # If the score is between 60 and 69, the grade is D
    print("Grade: D")
else:
    # If the score is less than 60, the grade is F
    print("Grade: F")