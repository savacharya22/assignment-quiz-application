from main_menu import create_menu, choose_quiz, display_question, get_user_choice, console, Prompt, clear_screen
from score import high_scores, save_score
import random


def run_quiz(quiz_function):

    qlist = list(quiz_function().keys())

    random.shuffle(qlist)
    score = 0
    while True:

        name = Prompt.ask("[bold blue]Enter your name  ")
        if name.strip() and all(char.isalpha() or char.isspace() for char in name):
            break
        else:
            print("Name has to be string. Enter your name")

    for idx, randnum in enumerate(qlist, start=1):

        display_question(idx, quiz_function()[randnum])
        user_choice = get_user_choice()

        if user_choice == quiz_function()[randnum]['correct']:
            console.print("Correct!!!", style="yellow")
            score = score + 1
        else:
            console.print("Wrong answer! ", style="red")
            console.print(
                f"Correct answer is {quiz_function()[randnum]['correct']}", style="green")

    print("-"*30)


    console.print(name, "Your score is  ", score, style="bold yellow")
    print()
    console.print("Thanks quiz is over", style="yellow on green")
    print()
    input("Press Enter to return to the main menu  ")
    clear_screen()

    return name, score


def main():
    while True:

        create_menu()
        user_option = Prompt.ask("[bold green]Enter your option")
        print()
        if user_option == "3":
            high_scores()
            input("Press Enter to return to the main menu")
            clear_screen()

        elif user_option == '4':
            console.print("Exit the game. See you again", style="bold red")
            break

        else:
            quiz_function = choose_quiz(user_option)
            if quiz_function:
                name, score = run_quiz(quiz_function)
                save_score(name, score)


main()
