"""
The game asks a user whether they want to play, they get a few questions and after finishing they get results in the form of a percentage.
"""
print("Welcome to the quiz!")
play = input("Do you want to play? ")
if play.lower() != "yes":
    quit()
score = 0


answer = input("What is the capital of Kenya? ")
if answer.lower() == "nairobi":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What ocean does Kenya have? ")
if answer.lower() == "indian":
    print('Correct')
    score += 1
else:
    print('Incorrect')

print("You got " + str(score) + " questions correct.")
print("You got " + str((score/2) * 100) + " %")