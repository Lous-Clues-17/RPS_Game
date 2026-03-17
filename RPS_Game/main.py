import random

def play_game():
    # Define the game options
    options = ['rock', 'paper', 'scissors'] 

    # Prompt user input, validate and convert to lowercase
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in options:
        print("Error: Invalid choice. Please try again with a valid option")
        return
    
    # Generate computer choice
    computer_choice = random.choice(options)
    
    # Display selections
    print(f"\nYou chose: {user_choice}")
    print(f"\nComputer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock') :
            print("You win!")
    else: 
         print("The computer wins!")
    
# Run game
if __name__ == '__main__':     
     play_game()



