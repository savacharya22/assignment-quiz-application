import random
import os

  

def create_menu():
    print("1. Enter 1 to choose Movie Quiz")
    print("2. Enter 2 to choose Science Quiz")
    print("3. Enter 3 to choose Music  Quiz")
    print("4. Enter 4 to choose Sports Quiz")
    print("5. Enter 5 to view High Scores")
    print("6. Enetr 6 to Exit Quiz")
    
    
def movie_quiz():
    questions = {
    1: {
        'que': 'What is the capital of Japan?',
        'a': 'Beijing',
        'b': 'Seoul',
        'c': 'Tokyo',
        'd': 'Bangkok',
        'correct': 'c'
    },
    2: {
        'que': 'Which element has the chemical symbol "O"?',
        'a': 'Oxygen',
        'b': 'Gold',
        'c': 'Silver',
        'd': 'Carbon',
        'correct': 'a'
    },
    3: {
        'que': 'Who wrote "Romeo and Juliet"?',
        'a': 'Charles Dickens',
        'b': 'Jane Austen',
        'c': 'William Shakespeare',
        'd': 'Mark Twain',
        'correct': 'c'
    },
    4: {
        'que': 'What is the largest mammal on Earth?',
        'a': 'Elephant',
        'b': 'Blue Whale',
        'c': 'Giraffe',
        'd': 'Hippopotamus',
        'correct': 'b'
    },
    5: {
        'que': 'Which planet is known as the "Morning Star" or "Evening Star"?',
        'a': 'Mars',
        'b': 'Venus',
        'c': 'Jupiter',
        'd': 'Saturn',
        'correct': 'b'
    },
    6: {
        'que': 'In what year did the Titanic sink?',
        'a': '1912',
        'b': '1923',
        'c': '1905',
        'd': '1931',
        'correct': 'a'
    },
    # Add more questions as needed
    
    
}
    return questions


def science_quiz():
    pass

def sports_quiz():
    pass

def music_quiz():
    pass

def choose_quiz(option):
    if option == '1':
        return movie_quiz
    elif option == '2':
        return science_quiz
    elif option == '3':
        return sports_quiz
    elif option == '4':
        return music_quiz
    else:
        print("Invalid Option. Please choose a valid Quiz")
        return None

def display_question(question_number, question):
    
    print("-"*30)
    print()
    print(f"Question {question_number} ): {question['que']}")
    print()
    print("\ta.", question['a'])
    print("\tb.", question['b'])
    print("\tc.", question['c'])
    print("\td.", question['d'])
    print()
 
  
  

def get_user_choice():
    while True:
        
        choice = input("Enetr your choice (a/b/c/d): ").lower()
        if choice in ['a', 'b', 'c', 'd']:
            return choice
        else:
            print("Invalid choice. Please enetr a, b, c, d")
            
def clear_screen():
    # clear screen based on operating system
    
    os.system('cls' if os.name == 'nt' else 'clear')
    

    
            
def run_quiz():
            
   
    qlist = list(questions.keys())
    random.shuffle(qlist)
    score = 0
    name = input("Enter your name :  ")


    for idx, randnum in enumerate(qlist, start = 1):
        clear_screen()
        display_question(idx, movie_quiz()[randnum])
        user_choice = get_user_choice()
        
        if user_choice == movie_quiz()[randnum]['correct']:
            print("Correct!")
            score = score + 1
        else:
            print("Wrong answer! ")

    print("-"*30)
            
    print(name, "Your score is  ", score)
    print("Thanks quiz is over")
   
   
run_quiz()