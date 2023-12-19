from data import movie_quiz, science_quiz
import random

import json
import pandas as pd



    



def create_menu():
    print("Welcome yo my quiz app!!!")
   
    print("1. Enter 1 to choose Movie Quiz")
    print("2. Enter 2 to choose Science Quiz")
    print("3. Enter 3 to view High Scores")
    print("4. Enterr 4 to Exit Quiz")
  

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
            

def high_scores():
    print("Inside high_scores function")
    try: 
        with open("scores.json", "r") as f:
            scores = json.load(f)
            if not scores:
                print("No scores yet")
            else:
                
                df = pd.DataFrame(scores)
                df = df.sort_values(by='score', ascending=False)
                print("Leaderboard:")
                print(df.to_string(index=False))

            
       
           
            
    except FileNotFoundError:
        scores = []
        with open("scores.json", "w") as f:
            json.dump(scores, f)
  
  
            
     

            
def save_score(name, score):
    try: 
        with open("scores.json", 'r') as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores =[]
        
    scores.append({'name': name, 'score': score})
    
    with open('scores.json', 'w') as f:
        json.dump(scores, f)
   

def high_scores():
    print("Inside high_scores function")
    try: 
        with open("scores.json", "r") as f:
            scores = json.load(f)
            if not scores:
                print("No scores yet")
            else:
                
                df = pd.DataFrame(scores)
                df = df.sort_values(by='score', ascending=False)
                print("Leaderboard:")
                print(df.to_string(index=False))

            
       
           
            
    except FileNotFoundError:
        scores = []
        with open("scores.json", "w") as f:
            json.dump(scores, f)
            
        if not scores:
            print("No scores yet")
        else:
            df = pd.DataFrame(scores)
            df = df.sort_values(by='score', ascending=False)
            print("Leaderboard:")
            print(df.to_string(index=False))

            
def save_score(name, score):
    try: 
        with open("scores.json", 'r') as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores =[]
        
    scores.append({'name': name, 'score': score})
    
    with open('scores.json', 'w') as f:
        json.dump(scores, f)
   
   
      

def create_menu():
    print("Welcome yo my quiz app!!!")
   
    print("1. Enter 1 to choose Movie Quiz")
    print("2. Enter 2 to choose Science Quiz")
    print("3. Enter 3 to view High Scores")
    print("4. Enterr 4 to Exit Quiz")
  

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
            

    
    
def main():
    while True:
        
        create_menu()
        user_option = input("Enter your option")
        if user_option == "3":
           high_scores()
           input("Press Enetr to return to the main menu")
          
        elif user_option == '4':
            print("Exit the game. See you again")
            break
            
        else:
            quiz_function = choose_quiz(user_option)
            if quiz_function:
                name, score =run_quiz(quiz_function)
                save_score(name, score)
               
                
            
def run_quiz(quiz_function):
            
   
    qlist = list(quiz_function().keys())
    random.shuffle(qlist)
    score = 0
    name = input("Enter your name : ")
   
    
    for idx, randnum in enumerate(qlist, start = 1):
      
        display_question(idx, quiz_function()[randnum])
        user_choice = get_user_choice()
        
        if user_choice == quiz_function()[randnum]['correct']:
            print("Correct!")
            score = score + 1
        else:
            print("Wrong answer! ")
            print(f"Correct answer is {quiz_function()[randnum]['correct']}")
      
    print("-"*30)
            
    print(name, "Your score is  ", score)
    print("Thanks quiz is over")
    input("Press Enetr to return to the main menu")
    
    return name, score
   
main()