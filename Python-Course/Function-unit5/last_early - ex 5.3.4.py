def last_early(my_str):

    if my_str[-1] in my_str[:-1:1]:
        print("True")
    else:
        print("False")

last_early(my_str=input("Please enter word: "))