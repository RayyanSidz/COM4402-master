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
        },
        {
            # Question 6:
            "question": "What's the highest rated movie on IMDB?",
            "options": ["1) The Shawshank Redemption", "2) The Godfather", "3) Inception",
                        "4) The Dark Knight"],
            "answer": 1
        },
        {
            # Question 7:
            "question": "Who was the leader of the Mongols?",
            "options": ["1) Joseph Stalin", "2) King Canute", "3) Genghis Khan",
                        "4) Zeus"],
            "answer": 3
        }
        ]

# Function to show the candidate's score
def show_score(score):
    # to allow the quiz variable to be used inside the function
    global quiz
    print(f"You scored {score} / {len(quiz)}")

# Function to run the quiz
def run_quiz():
    # Randomly shuffle the questions
    random.shuffle(quiz)
    score = 0

    # loop through each question in the quiz
    for index in range(len(quiz)):
        # display the question and the multiple choice options
        print(f"{index + 1}) {quiz[index]['question']}")
        print(quiz[index]['options'])
        user_answer = get_user_answer() # function defined in a later snippet of code
        # Only check the answer if it of the right datatype
        if user_answer != None:
            # To ensure the choice is within the range of options available
            if 0 < user_answer < 5:
                if user_answer == quiz[index]['answer']:
                    score += 1
            else:
                print("option doesn't exist")
                break
        else:
            # prompt the user with a choice to play again
            play_again()
            # End the function if the user clicks no
            return
    # Run the show score function to display the user's final score
    show_score(score)
    # prompt the user with a choice to play again
    play_again()

# Function to get the answer from the user
def get_user_answer():
    # Use of error handling to accept only integer inputs
    try:
        return int(input("Choose your answer: "))
    except ValueError:
        print("Invalid type")
        return None

# Function to enable the user to replay the quiz
def play_again():
    # prompt the user to play again
    run_quiz_again = input("Play again? Y/N: ")
    # Use of a conditional to either run or end the function based
    # on the user's input
    if run_quiz_again.lower() == "y":
        run_quiz()
    else:
        print("Goodbye!")

run_quiz()









