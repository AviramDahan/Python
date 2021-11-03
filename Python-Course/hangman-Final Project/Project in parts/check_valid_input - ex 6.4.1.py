def check_valid_input(letter_guessed, old_letters_guessed):

    """Receipt of the user character, checking whether he meets the conditions + adding it to the list of received characters.
    :param letter_guessed, old_letters_guessed
    :type Str
    :return True or false and adding to old list
    """

    #Check that the number of characters entered does not exceed 1, and that a character and not a number were entered.
    if len ( letter_guessed ) != 1:
        print ( False ,'\n' , old_letters_guessed )

    #Check if the char is not alpha char
    elif not letter_guessed.isalpha():
        print ( False ,'\n' , old_letters_guessed )

    # Check if the inserted character does not already exist in the inserted characters.
    elif letter_guessed in old_letters_guessed:
        print( False ,'\n' ,old_letters_guessed )

    #Prints the inserted character, adds it to the list of inserted characters, prints TRUE and the list is updated.
    else:
        print ( letter_guessed.lower () )
        old_letters_guessed += [letter_guessed]
        print(True , '\n' , old_letters_guessed)


def main():

   #Active function check_vaid_input
   check_valid_input(letter_guessed=input("Please enter a letter: "), old_letters_guessed=['s'])

   #Show documents help
   help(check_valid_input)

if __name__ == "__main__":
    main()