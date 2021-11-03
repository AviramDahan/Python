def is_valid_input(letter_guessed):

    """Receiving a written letter from the user, and checking the correctness of the conditions
    :param - letter_guessed
    :type - String
    :return - Returns true or false, depending on user input character and conditions
    """

    #Checking the correctness of inserting a character from the user (False Section)
    if len(letter_guessed) != 1 and letter_guessed.isalpha() == False:
     return print(False)

    elif len(letter_guessed) != 1:
     return print(False)

    elif not letter_guessed.isalpha():
     return print(False)

    # Checking the correctness of inserting a character from the user (True Section)
    else:
     print ("Letter: " + letter_guessed.lower())
     return print(True)


def main():

    #Active Function is_valid_input
    is_valid_input(letter_guessed=input("Please enter a letter: "))

    #Shows the documentation of the function.
    help(is_valid_input)

if __name__ == "__main__":
    main()



