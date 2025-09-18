import random

def hangman():
    # Predefined list of 5 words
    words = ["python", "apple", "school", "flower", "hangman"]
    word = random.choice(words)  # pick a random word
    
    guessed = []  # store guessed letters
    attempts = 6  # max incorrect guesses
    word_display = ["_"] * len(word)  # hidden word display
    
    print("Welcome to Hangman!")
    print("Guess the word:")
    print(" ".join(word_display))
    
    # Game loop
    while attempts > 0 and "_" in word_display:
        guess = input("\nEnter a letter: ").lower()
        
        # check valid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue
        
        if guess in guessed:
            print("You already guessed that letter.")
            continue
        
        guessed.append(guess)
        
        if guess in word:
            print("Correct guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
        
        print(" ".join(word_display))
    
    # End of game
    if "_" not in word_display:
        print("\n Congratulations! You guessed the word:", word)
    else:
        print("\n Game Over! The word was:", word)

# Run the game
hangman()

