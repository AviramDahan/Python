def format_list(my_list):

    """Print data from the list in the even positions, arranged with spaces and commas. + And the last data in the list with "and".
    :param - my_list , my_list_print
    :type - Str
    :return - Returns the list neatly according to the requirement.
    """
    #Setting the data in the even position with the addition of a space and a comma
    my_list_print = ", ".join(my_list[::2])

    #Returns the data with the addition of the last data in the list
    return my_list_print + " and " + my_list[-1]


def main():

    #Active function format_list
    print(format_list(my_list= ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))

    # Shows the documentation of the function.
    help(format_list)

if __name__ == "__main__":
    main()
