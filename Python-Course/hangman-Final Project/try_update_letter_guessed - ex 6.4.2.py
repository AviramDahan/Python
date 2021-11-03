def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Checks the correctness of the characters, and creates a list of characters.
     if FALSE creates a list with a separator '->'.
     If TRUE creates a regular list plus the character in it.
     :param - letter_guessed , old_letters_guessed
     :type - String
     :return - if false : 'X' (show to user worng input) and the list with -> separator , if true return the list with the new char
    """

    old_letters_guessed.sort ()

    #Check that the number of characters entered does not exceed 1, and that a character and not a number were entered.
    if len (letter_guessed) != 1:

        return print( 'X \n' ,' -> '.join(old_letters_guessed), '\n' ,  False)

    #Check if the char is not alpha char
    elif not letter_guessed.isalpha():

        return print( 'X \n' ,' -> '.join(old_letters_guessed), '\n' ,  False)

    # Check if the inserted character does not already exist in the inserted characters.
    elif letter_guessed in old_letters_guessed:

        return print( 'X \n' ,' -> '.join(old_letters_guessed), '\n' ,  False)


    #Prints the inserted character, adds it to the list of inserted characters, prints TRUE and the list is updated.
    else:
        print ( letter_guessed.lower () )
        old_letters_guessed.append(letter_guessed)
        old_letters_guessed.sort()
        return print(True , '\n' , old_letters_guessed)

def main():

   #Active function  try_update_letter_guessed
   try_update_letter_guessed(letter_guessed=input("Please enter a letter: ").lower(), old_letters_guessed=['s' , 'd'])


   #Show documents help
   help(try_update_letter_guessed)

if __name__ == "__main__":
    main()