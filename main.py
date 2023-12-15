import random
import os


    
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
    questions = {
    1: {
        "que": "What is the smallest planet in our solar system?",
        "a": "Mercury",
        "b": "Venus",
        "c": "Earth",
        "d": "Mars",
        "correct": "a"
    },
    2: {
        "que": "What is the process by which plants make their own food?",
        "a": "Photosynthesis",
        "b": "Respiration",
        "c": "Transpiration",
        "d": "Germination",
        "correct": "a"
    },
    3: {
        "que": "What is the main component of air?",
        "a": "Nitrogen",
        "b": "Oxygen",
        "c": "Carbon dioxide",
        "d": "Water vapor",
        "correct": "b"
    },
    4: {
        "que": "What is the largest bone in the human body?",
        "a": "Femur",
        "b": "Tibia",
        "c": "Humerus",
        "d": "Skull",
        "correct": "a"
    },
    5: {
        "que": "What is the study of rocks and minerals called?",
        "a": "Paleontology",
        "b": "Geology",
        "c": "Meteorology",
        "d": "Oceanography",
        "correct": "b"
    },
    6: {
        "que": "What is the process by which water changes from a liquid to a gas?",
        "a": "Condensation",
        "b": "Evaporation",
        "c": "Precipitation",
        "d": "Sublimation",
        "correct": "b"
    }
}
    return questions


def high_scores():
    pass

def create_menu():
    print("Welcome yo my quiz app!!!")
   
    print("1. Enter 1 to choose Movie Quiz")
    print("2. Enter 2 to choose Science Quiz")
    print("3. Enter 3 to view High Scores")
    print("4. Enetr 4 to Exit Quiz")
  




def choose_quiz(option):
    if option == '1':
        print("Welcome to a movie Quiz Game")
        return movie_quiz
    elif option == '2':
        print("Welcome to a science Quiz game!")
        return science_quiz
    
 
  
    else:
        print("Invalid Option. Please choose a valid Option")
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
    
    
def main():
    while True:
        
        create_menu()
        user_option = input("Enetr your option")
        if user_option == "3":
            return high_scores
        elif user_option == '4':
            print("Exit the game. See you again")
            break
        else:
            quiz_function = choose_quiz(user_option)
            if quiz_function:
                run_quiz(quiz_function)
            
        
    
    
    

    
            
def run_quiz(quiz_function):
            
   
    qlist = list(quiz_function().keys())
    random.shuffle(qlist)
    score = 0
    name = input("Enter your name : ")
   


    for idx, randnum in enumerate(qlist, start = 1):
        clear_screen()
        display_question(idx, quiz_function()[randnum])
        user_choice = get_user_choice()
        
        if user_choice == quiz_function()[randnum]['correct']:
            print("Correct!")
            score = score + 1
        else:
            print("Wrong answer! ")

    print("-"*30)
            
    print(name, "Your score is  ", score)
    print("Thanks quiz is over")
    input("Press Enetr to return to the main menu")
    
   
   
main()