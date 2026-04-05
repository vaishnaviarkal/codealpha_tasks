import random


def play_hangman():
    # 1. Setup: Predefined list of 5 words
    words=['python', 'coding', 'script', 'logic', 'system']
    secret_word = random.choice(words)
    
    # Track the letters guessed by the player
    guessed_letters=[]
    attempts_left = 6
    
    print("--- Welcome to Hangman! ---")
    
    # 2. Main Game Loop
    while attempts_left > 0:
        # Display the current progress (e.g., "p _ t h _ n")
        display_word = ""
        for char in secret_word:
            if char in guessed_letters:
                display_word += char + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")

        # Check if the player has won
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word!")
            break

        # 3. Handle Input
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        # 4. Check Guess (if-else logic)
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not there.")

    # 5. Game Over Logic
    if attempts_left == 0:
        print("\nGame Over!")
        print(f"The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()