import random

def guessing_game():
    secret_number = random.randint(1, 20)
    num_lives = 3
    
    print("Guess the secret number between 1 and 20.")
    
    while num_lives > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number between 1 and 20.")
            continue
        
        if guess < 1 or guess > 20:
            print("Your guess is out of the allowed range. Please guess a number between 1 and 20.")
            continue
        
        if guess > secret_number:
            print("Your guess is too high.")
            num_lives -= 1
        elif guess < secret_number:
            print("Your guess is too low.")
            num_lives -= 1
        else:
            print(f"Congratulations! You guessed the secret number: {secret_number}")
            break
        
        if num_lives > 0:
            print(f"You have {num_lives} {'life' if num_lives == 1 else 'lives'} remaining.")
    
    if num_lives == 0:
        print(f"Sorry, you've used all your lives. The secret number was {secret_number}. Better luck next time!")

# Start the game
guessing_game()

