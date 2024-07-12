''' Author- Jagu Manish || Python Programming Internship at CodSoft

------------------ TASK 4 - ROCK PAPER SCISSORS GAME -----------------------
User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for
the computer.
Game Logic: Determine the winner based on the user's choice and the
computer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores for
multiple rounds.
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and
feedback.

IDE used: Pycharm
Tip: Use VS Code for better performance.
'''



#importing modules
import random
import os

print('''
█▀█ █▀█ █▀▀ █▄▀     █▀█ ▄▀█ █▀█ █▀▀ █▀█      █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
█▀▄ █▄█ █▄▄ █ █     █▀▀ █▀█ █▀▀ ██▄ █▀▄      ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█ 
''')

print(" ╭────────────────────────────────────────────────────────────────────────────────────╮")
print(" │  Welcome to the Rock, Paper, Scissors game! In this game, there are 3 levels,      │")
print(" │  each consisting of 3 rounds. Scores will be awarded for each round, determining   │")
print(" │  the winner of that round. The total score determines the game winner!             │")
print(" ╰────────────────────────────────────────────────────────────────────────────────────╯")


def round_score():
    round_winner = " "

    if user_round_score < computer_round_score:
        round_winner = "COMPUTER WINS!"
    elif computer_round_score < user_round_score:
        round_winner = " PLAYER WINS! "
    else:
        round_winner = "     TIE!     "

    game_winner = " "
    if user_score < computer_score:
        game_winner = "COMPUTER WINS!"
    elif computer_score < user_score:
        game_winner = " PLAYER WINS! "
    else:
        game_winner = "     TIE!     "

    print("\n ")
    print("         ┌───────────────────────────────┐  ┌───────────────────────────────┐")
    print("         │           S C O R E           │  │   O V E R A L L   S C O R E   │")
    print("         ├───────────────────────────────┤  ├───────────────────────────────┤")
    print("         │                               │  │                               │")
    print(f"         │       PLAYER'S SCORE : {user_round_score}      │  │        PLAYER SCORE : {user_score}       │")
    print("         │                               │  │                               │")
    print(f"         │     COMPUTER'S SCORE : {computer_round_score}      │  │     COMPUTER'S SCORE : {computer_score}      │")
    print("         │                               │  │                               │")
    print("         ╞═══════════════════════════════╡  ╞═══════════════════════════════╡")
    print(f"         │        {round_winner}         │  │        {game_winner}         │")
    print("         └───────────────────────────────┘  └───────────────────────────────┘")

def game_score():
    game_winner = " "

    if user_score < computer_score:
        game_winner = "COMPUTER WINS!"
    elif computer_score < user_score:
        game_winner = " PLAYER WINS! "
    else:
        game_winner = "     TIE!     "

    print("\n ")
    print("         ┌───────────────────────────────┐")
    print("         │      T O T A L  S C O R E     │")
    print("         ├───────────────────────────────┤")
    print("         │                               │")
    print(f"         │        PLAYER SCORE : {user_score}       │")
    print("         │                               │")
    print(f"         │     COMPUTER'S SCORE : {computer_score}      │")
    print("         │                               │")
    print("         ╞═══════════════════════════════╡")
    print(f"         │        {game_winner}         │")
    print("         └───────────────────────────────┘")



Rock = '''
⠀⠀⠀⠀⠀⣠⡴⠖⠒⠲⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⣀⠔⠁⠀⠀  ⠈⠙⠷⣤⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⠞⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀  ⠘⢧ ⠈⢿⡀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠟⠛⠛⠃⠸⡇  ⠈⣇⠀
⣹⡷⠤⠤⠤⠄⠀⠀⠀⠀   ⢠⣤⡤⠶⠖⠛⣿⠀  ⣿⠀
⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⣠⡤⠖⠋⢀⣿ ⣠⠏⠀⠀
⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⣠⡾⠋⠁⠀⠀
⠀⠉⢿⡋⠉⠉⠁⠀⠀⠀⠀⠀  ⢀⣠⠾⠋⠀⠀⠀
⠀⠀⠈⠛⠶⠦⠤⠤⠤⠶⠶⠛⠋⠁⠀⠀⠀⠀⠀
'''
Paper = '''
⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠖⠒⢶⣄⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀
   ⢠⡶⠒⠳⠶⣄⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⣰⠏⠀⢀⣤⣤⣄⡀⠀⠀
   ⠸⡇⠀⠀⠀⠘⣇⠀⠀⣠⡾⠁⠀⠀⠀⢀⣾⣣⡴⠚⠉⠀⠀ ⠈⠹⡆⠀
⠀   ⢻⡄⠀⠀⠀⢻⣠⡾⠋⠀⠀⠀⠀⣠⡾⠋⠁ ⠀⠀⠀⠀⢀⣠⡾⠃⠀
    ⣿⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀  ⠀⠀⣠⠶⠋⠁⠀⠀⠀
   ⠠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀  ⢀⣴⡿⠥⠶⠖⠛⠛⢶⡄
   ⣰⡇⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀  ⢀⣠⠼⠃
⣿⠉⣇⠀⡴⠟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀  ⣀⣤⠶⠛⠉⠀⠀⠀
⢻⡄⠹⣦⠀⠶⠛⢁⣠⡴⠀⠀⠀⠀⠀⠀ ⣠⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀
 ⠻⣄⠈⢷⣄⠈⠉⠁⠀⠀⠀⢀⣠⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠉⠳⢤⣭⡿⠒⠶⠶⠒⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
Scissors = '''
⠀⠀⠀  ⢀⣠⣤⣀⣠⣤⠶⠶⠒⠶⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡴⠋⣠⠞⠋⠁⠀⠀⠀  ⠀⠙⣄⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡾⠁⣴⠋ ⠰⣤⣄⡀⠀⠀⠀⠀  ⠈⠳⢤⣼⣇⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠃⢰⠇⠰⢦⣄   ⡈⠉⠀⠀⠀⠀⠀⠀ ⠈⠉⠉⠉⠛⠛⠓⠲⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣧⣿⠀⠻⣤ ⡈⠛⠳⠆⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠹⣆⠀  ⠈⠛⠂⠀⠀⠀⠀⠀ ⠈⠐⠒⠒⠶⣶⣶⠶⠤⠤⣤⣠⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠈⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠐⠲⠤⣤⣀⡀⠀⠀⠀ ⠀ ⠈⠈⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀ ⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠤⠤⠤⠶⠞⠋⠉⠙⠳⢦⣄⡀⠀⠀⠀  ⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠈⠙⠳⠦⠾⠃⠀⠀⠀⠀⠀
'''
Game_emojis = [Rock, Paper, Scissors]



computer_score = 0
user_score = 0

computer_round_score = 0
user_round_score = 0
continue_game = True

while continue_game:
    level = 0
    while level <= 2:
        level += 1
        print("\n ")
        print("                           ╔════════════════════════════════╗")
        print(f"                           ║          L E V E L - {level}         ║")
        print("                           ╚════════════════════════════════╝")

        iterations = 1  # reset iterations counter at the start of each level of the game
        round = 0  # reset round counter at the start of each level of this game
        while iterations <= 3:
            round += 1
            print("\n")
            print(" ╭────────────────────────────────╮")
            print(f" │          R O U N D - {iterations}         │")
            print(" ╰────────────────────────────────╯")

            user_input = input("Enter your choice, Type: \n 0 for Rock.\n 1 for Paper.\n 2 for Scissors:  ").lower()
            try:
                user_choice = int(user_input)
                if user_choice not in [0, 1, 2]:
                    raise ValueError

                print(f"\nYour choice: {Game_emojis[user_choice]}")
                computer_choice = random.randint(0, 2)
                print(f"\nComputer's chose: {Game_emojis[computer_choice]}\n")
                if computer_choice == user_choice:
                    print("IT'S A DRAW!")
                elif computer_choice == 0 and user_choice == 2:
                    computer_round_score += 1
                    computer_score += 1
                    print("YOU LOST!")
                elif computer_choice == 2 and user_choice == 0:
                    user_round_score += 1
                    user_score += 1
                    print("YOU WON!")
                elif computer_choice > user_choice:
                    computer_round_score += 1
                    computer_score += 1
                    print("YOU LOST!")
                elif user_choice > computer_choice:
                    user_round_score += 1
                    user_score += 1
                    print("YOU WON!")
                iterations += 1
            except ValueError:
                print("Invalid input! Please enter a number.")
        round_score()
        computer_round_score = 0
        user_round_score = 0
    game_score()

    continue_playing = input("You've completed the game! Ready to challenge yourself again? (y/n) : ")
    if continue_playing == 'y':
        continue_game = True
        computer_score = 0
        user_score = 0
        os.system('cls') # Try ('clear') for linux, Mac users
    else:
        continue_game = False
        print("Game over! We hope you enjoyed playing. See you next time!")
        print("beep....beep....exited from the game!")
