"""Ex-O2: A program to guess the secret word!""" 

___author___ = "730403071"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)} letter guess? ")
cont: bool = True

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index_guess_word: int = 0  # A variable for keeping track of the index of guess
emoji: str = ""
index_secret_word: int = 0  # A variable for checking each index of the secret word

while cont:
    if guess == secret_word:
        while index_guess_word < len(secret_word):
            emoji += GREEN_BOX
            index_guess_word = index_guess_word + 1
        # seeing if it is the correct guess and if it's correct, it prints all green boxes 
        print(emoji)           
        print("Woo! You got it!")
        cont = False  # ends the loop if the guess was correct 
    elif len(guess) != len(secret_word):  # checking the length of guess 
        guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")
    elif len(guess) == len(secret_word):  # while the length is correct, comparing the guess index to the indices of the secret word
        
        while index_guess_word < len(secret_word):
            if index_secret_word == len(secret_word):  # goes through the length of the word and doesn't find anything 
                emoji += WHITE_BOX
                index_secret_word = 0
                index_guess_word = index_guess_word + 1
            elif guess[index_guess_word] != secret_word[index_secret_word]:  # checking to see if the index i of  guess is not equal to index j or secret word
                index_secret_word = index_secret_word + 1
            elif guess[index_guess_word] == secret_word[index_secret_word] and index_secret_word == index_guess_word:  # true if indices are found in both word and in same index location 
                emoji += GREEN_BOX
                index_guess_word = index_guess_word + 1
            elif guess[index_guess_word] == secret_word[index_secret_word]:  # sees if the same index is found but in different location 
                emoji += YELLOW_BOX
                index_secret_word = 0
                index_guess_word = index_guess_word + 1
            #  looping to compare the indices of both the guess and secret word 
       
        print(emoji)        
        print("Not quite. Play again soon")
        cont = False