"""
Quiz Game (OOP Version)

Overview:
---------
This script initializes and runs a quiz game built using Object-Oriented Programming.
It converts raw question data into Question objects and uses a QuizBrain class
to manage the quiz flow, user interaction, and scoring.

Flow:
-----
- Load question data
- Create Question objects and store in a question bank
- Initialize QuizBrain with the question bank
- Loop through questions while available
- Display final score at the end

Notes:
------
- Separates concerns using classes (Question, QuizBrain)
- Promotes clean, modular, and maintainable code structure
"""


from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
