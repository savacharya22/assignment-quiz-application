from data import movie_quiz, science_quiz
import os
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
    console.print("2. Enter 2 to choose Science Quiz", style = "dodger_blue1")
    console.print("3. Enter 3 to view High Scores", style =" medium_spring_green")
    console.print("4. Enter 4 to Exit Quiz", style = "dark_slate_gray2")
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
      
        choice = Prompt.ask("[bold plum2]Enter your choice (a/b/c/d) ")
        if choice in ['a', 'b', 'c', 'd']:
            return choice
        else:
            console.print("Invalid choice. Please enter a, b, c, d", style ="bold green")
            



   
      

  

def choose_quiz(option):
    if option == '1':
        clear_screen()
        console.print("Welcome to a movie Quiz Game", style= "bold green3 underline")
        print()
        return movie_quiz
    elif option == '2':
        clear_screen()
        console.print("Welcome to a science Quiz game!", style = "bold underline cyan")
        print()
        return science_quiz
  
    else:
        clear_screen()
        console.print("Invalid Option. Please choose a valid Option", style= "sea_green1 underline")
       
        return None
    
