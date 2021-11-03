guess_letter = input('Please Guess a letter: ')

if len(guess_letter) != 1 and guess_letter.isalpha() == False:
    print('E3')
elif len(guess_letter) != 1:
    print('E1')
elif not guess_letter.isalpha():
    print('E2')

else:
    print(guess_letter.lower())