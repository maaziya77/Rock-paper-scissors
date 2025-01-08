import random

ROCK = 'rock'
PAPER = 'paper'
SCISSOR = 'scissor'
choices = [ROCK, PAPER, SCISSOR]
positive = [[PAPER, ROCK], [SCISSOR, PAPER], [ROCK, SCISSOR]]
negative = [[ROCK, PAPER], [PAPER, SCISSOR], [SCISSOR, ROCK]]

def get_computer_move():
    return random.choice(choices)

def find_winner(user_move, computer_move):
    if [user_move, computer_move] in positive:
        return 1
    elif [user_move, computer_move] in negative:
        return -1
    return 0

# Personalized welcome message
print("===== Welcome to Rock, Paper, Scissors Game =====")
user_name = input("What's your name? ").strip()

# Initialize scores
user_score = 0
computer_score = 0

while True:
    choice = input(f"\nHi {user_name}, do you wanna play (y/n): ").strip().lower()
    
    if choice == 'y':
        computer_move = get_computer_move()
        while True:
            move = input(f"\n{user_name}, select a move ('r' for rock / 'p' for paper / 's' for scissor): ").strip().lower()
            if move in ['r', 'p', 's']:
                user_move = {'r': ROCK, 'p': PAPER, 's': SCISSOR}[move]
                print(f"\n{user_name}'s Move: {user_move.capitalize()}")
                print(f"Computer's Move: {computer_move.capitalize()}")
                
                output = find_winner(user_move, computer_move)
                
                if output == 1:
                    user_score += 1
                    print(f"\n{user_name} Won !!!")
                elif output == -1:
                    computer_score += 1
                    print("\nComputer Won !!!")
                else:
                    print("\nIt's a Tie !!!")
                
                # Display scores after each round
                print(f"\n{user_name}'s Score: {user_score} | Computer's Score: {computer_score}")
                break
            else:
                print("Invalid input...please try again")
    elif choice == 'n':
        print(f"\nExiting... Thanks for playing, {user_name}!")
        print(f"Final Score: {user_name} - {user_score} | Computer - {computer_score}")
        break
    else:
        print("Invalid input...please try again")

