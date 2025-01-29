"""
pip install termcolor 
Define questions, options and correct answers
Shuffle the questions
Loop through the questions
  Print the question
  Get the answer from the user
  Check if the answer is correct
    Print the result
    Increment the score
  Else
    Print the result
Print the final score
"""
import random
from termcolor import cprint

quiz = [
    {
        "question": "What is the capital of Kenya?",
        "options": ["Nairobi", "Mombasa", "Kisumu", "Eldoret"],
        "answer": "Nairobi"
    },
    {
        "question": "What ocean does Kenya have?",
        "options": ["Indian", "Pacific", "Atlantic", "Arctic"],
        "answer": "Indian"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Dollar", "Pound", "Shilling", "Yen"],
        "answer": "Yen"
    },
    {
        "question": "What is the tallest mountain in Kenya?",
        "options": ["Mount Kenya", "Mount Elgon", "Mount Longonot", "Mount Meru"],
        "answer": "Mount Kenya"
    },
    {
        "question": "What is the largest city in Kenya?",
        "options": ["Nairobi", "Mombasa", "Kisumu", "Eldoret"],
        "answer": "Nairobi"
    }
]

random.shuffle(quiz)
score = 0

for index, item in enumerate(quiz):
    print(f"Question {index + 1}: {item['question']}")
    for option in item['options']:
        print(option)

#User input
    answer = input("Enter your answer: ").strip()
    if answer == item['answer']:
        cprint("Correct!", "green")
        score += 1
    else:
        cprint(f"Incorrect! The correct answer is {item['answer']}", "red")


print() #To make output clear
print(f"Your final score is {score} out of {len(quiz)}")