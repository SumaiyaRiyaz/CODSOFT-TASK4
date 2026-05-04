import random

def get_user_choice():
    # Function to get user's choice
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    # Function to get computer's choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    return computer_choice

def determine_winner(user_choice, computer_choice):
    # Function to determine the winner
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "Congratulations! You won!"
    else:
        return "Sorry! You lost."

def play_game():
    # Main function to play the game
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
