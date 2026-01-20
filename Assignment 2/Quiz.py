# Console based Quiz
import random

# A list of question, options and the correct answers
quiz = [
        {
            # Question 1:
            "question": "What company is PlayStation from?",
            "options": ["Microsoft", "Sony", "Meta", "Dodge"],
            "answer": 2
        },
        {
            # Question 2:
            "question": "What game won game of the year 2022?",
            "options": ["GOW Ragnarok", "Elden Ring", "Stray", "Horizon: Forbidden West"],
            "answer": 2
        },
        {
            # Question 3:
            "question": "Who is the best chess player in the world?",
            "options": ["Anatoly Karpov", "Hikaru Nakamura", "Magnus Carlson", "Oppenheimer"],
            "answer": 3
        },
        {
            # Question 4:
            "question": "Which of one these Companies is German?",
            "options": ["Siemens", "Gymshark", "Meta", "Ubisoft"],
            "answer": 1
        },
        {
            # Question 5:
            "question": "Which one of these cities is located in the Middle East?",
            "options": ["Sao Paulo", "Bangkok", "Manchester", "Sharjah"],
            "answer": 4
        }
        ]

# Function to run the quiz
def run_quiz():
    #Randomly shuffle the questions
    random.shuffle(quiz)

    for index in range(len(quiz)):
        print(f"{index + 1}) {quiz[index]['question']}")
        answer = input(f"{quiz[index]['options']}")
        try:
            user_answer = int(answer)
        except ValueError:
            user_answer = answer



