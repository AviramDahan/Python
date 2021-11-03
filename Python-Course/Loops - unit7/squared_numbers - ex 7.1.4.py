def squared_numbers(start, stop):

    """Receiving two numbers, and performing each number squared from beginning to end,
     each number on its own. And entering the list and returning the list.
     :param - i , list_results , Start_squared , start , stop
     :type - int = start , stop , i , list_results , Start_squared
     :return - list_results updated with the numbers squared inside
     """

    #Creating parameters for use within the loop, count + list
    i = start
    list_results = []


    #The While loop, which begins with i which is equal to the first number entered (Start),
    # and is executed until the last number entered (Stop) includes.
    while i != stop+1:

        #Create a variable to add to a list + insert into a list using append
        Start_squared = start ** 2
        list_results.append(Start_squared)

        #Progress in the round
        i += 1
        start += 1

    #Returns the final array, with the results
    return print(list_results)

def main():

   #Active function  squared_numbers
   squared_numbers(start=int(input("Please enter Start: ")), stop=int(input("Please enter Stop: ")))

   #Show documents help
   help(squared_numbers)

if __name__ == "__main__":
    main()