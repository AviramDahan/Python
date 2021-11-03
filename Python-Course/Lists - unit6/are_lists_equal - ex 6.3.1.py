def are_lists_equal(list1, list2):

    """Check for a match between two lists , first sort then check.
    :param - list1 , list2
    :type - int , float
    :return - True if match ,False if not
    """

    #Sort before check
    list1.sort()
    list2.sort()

    #after lists sort, now we check
    if list2[:] == list1[:]:
        return print(True)

    else:
        return print(False)

def main():

    #Active function are_lists_equal
    are_lists_equal(list1=[0.6, 1, 2, 3], list2=[3, 2, 0.6, 1])

    # Shows the documentation of the function.
    help(are_lists_equal)

if __name__ == "__main__":
    main()