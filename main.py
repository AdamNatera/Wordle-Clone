def main():
    # initialize game
    game_over = False
    wordle = "boner"
    max_guesses = 6
    guess_counter = 0

    # game loop
    while not game_over:
        print("""
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+""")
        guess_valid = False
    
        while not guess_valid:
            guess = input("Enter your guess: ").strip().lower()
        
            if len(guess) != 5:
                print("Error: Guess must contain exactly 5 letters")
                continue # ask for input again if wrong
            
            if not guess.isalpha():
                print("Error: Guess must only contain letters")
                continue # ask for input again if wrong
                
            break

    
    


if __name__ == "__main__":
    main()
