from data import movie_quiz, science_quiz
from score import high_scores, save_score
import os
import random

from rich.console import Console
from rich.prompt import Prompt
console = Console()



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')





def create_menu():
    print()
    print()
    console.print("Welcome yo my quiz app!!!", style="bold underline green on white")
    print()
    console.print("1. Enter 1 to choose Movie Quiz", style = "yellow")
    console.print("2. Enter 2 to choose Science Quiz")
    console.print("3. Enter 3 to view High Scores")
    console.print("4. Enter 4 to Exit Quiz")
    print()
    
  


    

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
      
        choice = Prompt.ask("[bold yellow]Enetr your choice (a/b/c/d): ")
        if choice in ['a', 'b', 'c', 'd']:
            return choice
        else:
            console.print("Invalid choice. Please enter a, b, c, d", style ="bold green")
            



   
      

  

def choose_quiz(option):
    if option == '1':
        console.print("Welcome to a movie Quiz Game", style= "bold green3 underline")
        print()
        return movie_quiz
    elif option == '2':
        console.print("Welcome to a science Quiz game!", style = "bold underline cyan")
        print()
        return science_quiz
  
    else:
        console.print("Invalid Option. Please choose a valid Option", style= "green on cyan")
        return None
    




    
    
def main():
    while True:
        
        create_menu()
        user_option = Prompt.ask("[bold green]Enter your option")
        print()
        if user_option == "3":
           high_scores()
           input("Press Enter to return to the main menu")
          
        elif user_option == '4':
            console.print("Exit the game. See you again", style = "bold red")
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
    name = Prompt.ask("[bold blue]Enter your name : ")
   
    
    for idx, randnum in enumerate(qlist, start = 1):
      
        display_question(idx, quiz_function()[randnum])
        user_choice = get_user_choice()
        
        if user_choice == quiz_function()[randnum]['correct']:
            console.print("Correct!!!", style= "yellow")
            score = score + 1
        else:
            console.print("Wrong answer! ", style ="red")
            console.print(f"Correct answer is {quiz_function()[randnum]['correct']}", style = "green")
      
    print("-"*30)
            
    console.print(name, "Your score is  ", score, style = "bold yellow")
    print()
    console.print("Thanks quiz is over", style = "yellow on green")
    print()
    input("Press Enter to return to the main menu  ")
    clear_screen()
    
    return name, score
   
main()