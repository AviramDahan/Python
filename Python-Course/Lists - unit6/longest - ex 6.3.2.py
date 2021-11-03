def longest(my_list):

    """return the longest in list , first sort then print (the sort doing from small to big , so print the last [-1]
    :param - my_list
    :type - int , str
    :return - the longest in the list
    """
    #sort by len small to big
    my_list.sort(key=len)

    #return the last in list (the biggest)
    return my_list[-1]


def main():

    #Active function longest
    print(longest(my_list = ["111", "234" ,"2000" ,"goru" ,"birthday" ,"09"]))

    # Shows the documentation of the function.
    help(longest)

if __name__ == "__main__":
    main()