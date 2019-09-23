# Problem Set 2, hangman.py
# Name: Minh Vu
# Collaborators:
# Time spent: 12 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # iterates through each letter of the secret word
    for element in secret_word:
        # if only one letter is not in the guessed list
        if element not in letters_guessed:
            return False
        
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    # this will be our result string, which starts as an empty string
    result = ""
    for element in secret_word:
        if element not in letters_guessed:
            result += "_ "
        else:
            result += element
            
    return result


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    result = string.ascii_lowercase
    
    for element in letters_guessed:
        result = result.replace(element, "")
    
    return result
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guess_left = 6
    warnings_left = 3
    letters_guessed = []
    current_secret_word = "" 
    available_letters = string.ascii_lowercase
    print("Welcome to the game of Hangman!")
    print("The secret word will have " + str(len(secret_word)) + " letters")
    
    success = False
    char_is_valid = True
    while not success and guess_left > 0: 
        print("You have " + str(guess_left) + " guesses left.")
        print("Available letters: " + available_letters)
        # take input 
        guessed_char = str.lower(input("Please guess a letter: "))
        # check if input is in alphabet
        char_is_valid = str.isalpha(guessed_char)
        
        # check to see if that letter is already been guessed (except if it's a "*")
        char_is_already_guessed = guessed_char in letters_guessed
        
         # check symbol validity
        if not char_is_valid:
            if warnings_left == 0:
                guess_left -= 1
            else:
                warnings_left -= 1
            print("Oops! That's not a valid letter. You now have " + str(warnings_left) + " warnings: " + current_secret_word)
            continue
        
        # add that letter into the list of letters that have been guessed
        if not char_is_already_guessed: 
            letters_guessed.append(guessed_char)
        else: # and update warning_left and guess_left
            if warnings_left == 0: 
                guess_left -= 1
            else:
                warnings_left -= 1
            print("Oops! You've already guessed that letter. You now have " + str(warnings_left) + " warnings: " + current_secret_word)
            continue
            
        print(letters_guessed)
        
        # update available letters
        available_letters = get_available_letters(letters_guessed)
        # this is to show the user
        current_secret_word = get_guessed_word(secret_word, letters_guessed)
        
        # now check to see if the guessed letter is in the secret word
        if guessed_char not in secret_word:
            if guessed_char in CONSONANTS:
                guess_left -= 1
            else:
                guess_left -= 2
            print("Oops! That letter is not in my word: " + current_secret_word)
        else: 
            print("Good guess: " + current_secret_word)
            
        success = is_word_guessed(secret_word, letters_guessed)
        print("------------------------")
         
       
    # decide if they won or not
    if success:
        # count the number of distinct letter
        unique = []
        for x in letters_guessed:
            if x in secret_word and x not in unique:
                unique.append(x)
        
        # compute score
        score = guess_left*len(unique)
        print("Congratulation, you won!")
        print("Your total score for this game is: " + str(score))
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")

    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

# helper function to check if the hidden letter is already been revealed 
def hidden_is_already_revealed(my_word, other_word):
    my_word_without_space = my_word.replace(" ", "") 
    guessed_char_in_my_word = []
    
    # fill the list with all the letters that have 
    # already been revealed in my word
    for element in my_word_without_space:
        if (element != "_") and (element not in guessed_char_in_my_word):
            guessed_char_in_my_word.append(element)
    
    
    for i in range (len(other_word)):
        if my_word_without_space[i] == "_" and (other_word[i] in guessed_char_in_my_word):
            return True

    return False
      


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    my_word_without_space = my_word.replace(" ", "") 
    # first, check if they have the same length 
    if len(my_word_without_space) != len(other_word):
        return False
    
    # check if the hidden letter is one of the letters 
    # that has already been revealed
    if hidden_is_already_revealed(my_word_without_space, other_word):
        return False
    
    # finally, just check if those 2 words match
    index = -1
    for element in my_word_without_space:
        index += 1
        if element != "_" and element != other_word[index]:
            return False
        
    return True
    

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    possible_match = []
    
    # go through word list 
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_match.append(word) 
    
    if len(possible_match) == 0:
        print("No matches found")
        return
    
    # print out all the possible match    
    for word in possible_match:
        print(word, end = ' ') 


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    guess_left = 6
    warnings_left = 3
    letters_guessed = []
    current_secret_word = "" 
    available_letters = string.ascii_lowercase
    print("Welcome to the game of Hangman!")
    print("The secret word will have " + str(len(secret_word)) + " letters")
    
    success = False
    char_is_valid = True
    while not success and guess_left > 0: 
        print("You have " + str(guess_left) + " guesses left.")
        print("Available letters: " + available_letters)
        # take input 
        guessed_char = str.lower(input("Please guess a letter: "))
        # check if input is in alphabet
        if guessed_char == "*":
            char_is_valid = True
        else:    
            char_is_valid = str.isalpha(guessed_char)
        
        # check to see if that letter is already been guessed (except if it's a "*")
        char_is_already_guessed = guessed_char in letters_guessed
        
         # check symbol validity
        if not char_is_valid:
            if warnings_left == 0:
                guess_left -= 1
            else:
                warnings_left -= 1
            print("Oops! That's not a valid letter. You now have " + str(warnings_left) + " warnings: " + current_secret_word)
            continue
        
        # add that letter into the list of letters that have been guessed
        if guessed_char == "*":
            pass
        elif not char_is_already_guessed: 
            letters_guessed.append(guessed_char)
        else: # and update warning_left and guess_left
            if warnings_left == 0: 
                guess_left -= 1
            else:
                warnings_left -= 1
            print("Oops! You've already guessed that letter. You now have " + str(warnings_left) + " warnings: " + current_secret_word)
            continue
            
        print(letters_guessed)
        
        # update available letters
        available_letters = get_available_letters(letters_guessed)
        # this is to show the user
        current_secret_word = get_guessed_word(secret_word, letters_guessed)
        
        # now check to see if the guessed letter is in the secret word
        if guessed_char == "*":
            print("Possible word matches are:")
            print(show_possible_matches(current_secret_word))
        elif guessed_char not in secret_word:
            if guessed_char in CONSONANTS:
                guess_left -= 1
            else:
                guess_left -= 2
            print("Oops! That letter is not in my word: " + current_secret_word)
        else: 
            print("Good guess: " + current_secret_word)
            
        success = is_word_guessed(secret_word, letters_guessed)
        print("------------------------")
         
       
    # decide if they won or not
    if success:
        # count the number of distinct letter
        unique = []
        for x in letters_guessed:
            if x in secret_word and x not in unique:
                unique.append(x)
        
        # compute score
        score = guess_left*len(unique)
        print("Congratulation, you won!")
        print("Your total score for this game is: " + str(score))
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
  