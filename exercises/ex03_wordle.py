"""Ex-03: A new and improved structured Wordle."""


__author__ = "730403071"


def contains_char(search: str, single_char: str) -> bool:
    """A function to evalute the given string for a char and either returns true or false."""
    assert len(single_char) == 1 
    i: int = 0
    while i < len(search): 
        if search[i] == single_char:
            return True 
        else: 
            i += 1  # Iterates in order to check each index of the word 
    return False 
# Defining a function to search for a character within a word by going through each index 


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str: 
    """Returns a string of emoji of different color codes."""
    assert len(guess) == len(secret) 
    i: int = 0  
    emoji: str = ""   
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        else: 
            test: bool = contains_char(secret, guess[i])
            if test:
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        i += 1

    return emoji 
# A function that produces the codified emoji to show which characters are either in the right spot, switched around, or not in the word at all


def input_guess(expected_length: int) -> str: 
    """Prompting for a guess until the user provides a guess of expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length: 
        guess = input(f"That wasn't {expected_length} chars! Try again: ") 

    return guess
# A function that returns messages relating to the length of the input (guess word) 
# Allows the user to put in words of different lengths and try again 


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    current_turn: int = 1
    correct_length: int = len(secret)
    result: bool = False
    while current_turn <= 6 and not result:  # A while loop for determining turn # and whether the guess is correct
        print(f"===Turn {current_turn}/6 ===") 
        guess_word = input_guess(correct_length)
        print(emojified(guess_word, secret))

        if guess_word == secret: 
            result = True  # This bool allows the program to exit the loop 
        else: 
            current_turn += 1 
    if result:  # If the guess is correct, this message results 
        print(f"You won in {current_turn}/6 turns!")
    else:  # If the user uses up all of the 6 turns, this message results 
        print("X/6 - Sorry, try again tomorrow!") 
  
# When the user either guesses the correct word or runs out of tries, the program exits the loop 


if __name__ == "__main__": 
    main()