import random
import time
import os

def clear_screen():
    """Clear the console screen based on the operating system."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def print_welcome():
    """Display the welcome message and game rules."""
    print("=" * 50)
    print("🎮 ROCK PAPER SCISSORS GAME 🎮")
    print("=" * 50)
    print("\n📋 GAME RULES:")
    print("• Rock crushes Scissors")
    print("• Scissors cuts Paper")
    print("• Paper covers Rock")
    print("• Same choices result in a tie!")
    print("\n🎯 HOW TO PLAY:")
    print("• Type 'r' for Rock")
    print("• Type 'p' for Paper")
    print("• Type 's' for Scissors")
    print("• Type 'q' to quit the game")
    print("• Type 'score' to see current scores")
    print("=" * 50)

def get_user_choice():
    """Get and validate user input."""
    while True:
        choice = input("\n🎯 Your choice (r/p/s/q/score): ").lower().strip()
        
        if choice == 'q':
            return 'quit'
        elif choice == 'score':
            return 'score'
        elif choice in ['r', 'p', 's']:
            return choice
        else:
            print("❌ Invalid choice! Please enter 'r', 'p', 's', 'q', or 'score'.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['r', 'p', 's']
    return random.choice(choices)

def get_choice_name(choice):
    """Convert choice abbreviation to full name."""
    choice_names = {
        'r': 'Rock',
        'p': 'Paper',
        's': 'Scissors'
    }
    return choice_names.get(choice, 'Unknown')

def get_choice_emoji(choice):
    """Get emoji representation for each choice."""
    emojis = {
        'r': '🪨',
        'p': '📄',
        's': '✂️'
    }
    return emojis.get(choice, '❓')

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the round."""
    if user_choice == computer_choice:
        return 'tie'
    
    winning_combinations = {
        'r': 's',  # Rock beats Scissors
        's': 'p',  # Scissors beats Paper
        'p': 'r'   # Paper beats Rock
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return 'user'
    else:
        return 'computer'

def display_round_result(user_choice, computer_choice, result):
    """Display the result of the current round."""
    print("\n" + "=" * 30)
    print("🎯 ROUND RESULT")
    print("=" * 30)
    
    user_emoji = get_choice_emoji(user_choice)
    computer_emoji = get_choice_emoji(computer_choice)
    
    print(f"👤 You chose: {get_choice_name(user_choice)} {user_emoji}")
    print(f"🤖 Computer chose: {get_choice_name(computer_choice)} {computer_emoji}")
    print()
    
    if result == 'tie':
        print("🤝 It's a tie!")
    elif result == 'user':
        print("🎉 You win this round!")
    else:
        print("😔 Computer wins this round!")
    
    print("=" * 30)

def display_score(user_score, computer_score, ties):
    """Display the current score."""
    print("\n" + "=" * 30)
    print("📊 CURRENT SCORE")
    print("=" * 30)
    print(f"👤 You: {user_score}")
    print(f"🤖 Computer: {computer_score}")
    print(f"🤝 Ties: {ties}")
    print("=" * 30)

def display_final_results(user_score, computer_score, ties):
    """Display the final game results."""
    print("\n" + "=" * 50)
    print("🏁 GAME OVER - FINAL RESULTS")
    print("=" * 50)
    
    total_games = user_score + computer_score + ties
    print(f"📈 Total games played: {total_games}")
    print(f"👤 Your wins: {user_score}")
    print(f"🤖 Computer wins: {computer_score}")
    print(f"🤝 Ties: {ties}")
    
    if total_games > 0:
        user_percentage = (user_score / total_games) * 100
        print(f"📊 Your win rate: {user_percentage:.1f}%")
    
    print()
    
    if user_score > computer_score:
        print("🎉 CONGRATULATIONS! You won the game!")
    elif computer_score > user_score:
        print("😔 Better luck next time! Computer won the game.")
    else:
        print("🤝 It's a tie game! Well played!")
    
    print("=" * 50)

def play_game():
    """Main game loop."""
    user_score = 0
    computer_score = 0
    ties = 0
    round_num = 1
    
    print_welcome()
    
    while True:
        print(f"\n🔄 ROUND {round_num}")
        print("-" * 20)
        
        user_choice = get_user_choice()
        
        if user_choice == 'quit':
            break
        elif user_choice == 'score':
            display_score(user_score, computer_score, ties)
            continue
        
        # Computer makes its choice
        computer_choice = get_computer_choice()
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        
        # Update scores
        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1
        else:
            ties += 1
        
        # Display result
        display_round_result(user_choice, computer_choice, result)
        
        # Display current score
        display_score(user_score, computer_score, ties)
        
        round_num += 1
        
        # Ask if user wants to continue
        if round_num > 1:
            continue_choice = input("\n🔄 Play another round? (y/n): ").lower().strip()
            if continue_choice not in ['y', 'yes']:
                break
    
    # Display final results
    display_final_results(user_score, computer_score, ties)
    
    # Goodbye message
    print("\n👋 Thanks for playing Rock Paper Scissors!")
    print("🎮 Come back soon for another game!")

def main():
    """Main function to start the game."""
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\n⚠️ Game interrupted by user.")
        print("👋 Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("👋 Please try running the game again.")

if __name__ == "__main__":
    main()
