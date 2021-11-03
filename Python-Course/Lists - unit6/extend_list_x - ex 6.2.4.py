def extend_list_x(list_x, list_y):
    """Consolidation of two lists into one list
    :param - list_x , list_y , United_List
    :type - int
    :return - the Merge List (United_List)
    """

    #Merge Lists
    United_List = [*list_y, *list_x]

    #Return the Merge List
    return United_List


def main():

    #Active function extend_list_x
    print(extend_list_x(list_x=[4, 5, 6], list_y=[1, 2, 3]))

    # Shows the documentation of the function.
    help(extend_list_x)

if __name__ == "__main__":
    main()