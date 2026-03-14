def main():
    # initialize game
    # Gay bois coding army
    # Make a function broooooo this is bad
    game_over = False
    wordle = "boner"
    max_guesses = 6
    guess_counter = 0

    # game loop
    while not game_over:
        # draw board
        # Put this in a function -DWS draw game function
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
        
        # user input
        # Put this in a function -DWS
        # Input validation is weak no checks for numbers or symbols -DWS
        # Put this into one function for input validaiton, one for a check against the solution word, and another for updating game state
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

        # evaluate guess
        # Make another function -DWS
        
    
    


if __name__ == "__main__":
    main()
