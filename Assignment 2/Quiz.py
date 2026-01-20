# Console based Quiz
import random

# A list of question, options and the correct answers
quiz = [
        {
            # Question 1:
            "question": "What company is PlayStation from?",
            "options": ["1) Microsoft", "2) Sony", "3) Meta", "3) Dodge"],
            "answer": 2
        },
        {
            # Question 2:
            "question": "What game won game of the year 2022?",
            "options": ["1) GOW Ragnarok", "2) Elden Ring", "3) Stray", "4) Horizon: Forbidden West"],
            "answer": 2
        },
        {
            # Question 3:
            "question": "Who is the best chess player in the world?",
            "options": ["1) Anatoly Karpov", "2) Hikaru Nakamura", "3) Magnus Carlson", "4) Oppenheimer"],
            "answer": 3
        },
        {
            # Question 4:
            "question": "Which of one these Companies is German?",
            "options": ["1) Siemens", "2) Gymshark", "3) Meta", "4) Ubisoft"],
            "answer": 1
        },
        {
            # Question 5:
            "question": "Which one of these cities is located in the Middle East?",
            "options": ["1) Sao Paulo", "2) Bangkok", "3) Manchester", "4) Sharjah"],
            "answer": 4
        }
        ]

# Function to run the quiz
def run_quiz():
    #Randomly shuffle the questions
    random.shuffle(quiz)
    score = 0
    for index in range(len(quiz)):
        print(f"{index + 1}) {quiz[index]['question']}")
        answer = input(f"{quiz[index]['options']}")
        try:
            user_answer = int(answer)
        except ValueError:
            user_answer = answer

        if 0 < user_answer > 5:
            if user_answer == quiz[index]['answer']:
                score += 1
        elif user_answer == quiz[index]['options'[quiz[index]['answer']]]:
            score



