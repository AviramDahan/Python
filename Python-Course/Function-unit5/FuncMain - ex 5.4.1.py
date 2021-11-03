def func(num1, num2):
    """Test result for two variables
    :param num1 and num2
    :type num1 and num2 = float
    :return RMTOTAL
    """
    RMTOTAL = num1+num2
    return RMTOTAL

def main():

    #Call Function func
   print(func(num1=float(input("Please enter first num: ")), num2=float(input("Please enter second num: "))))

    # Shows the documentation of the function.
   help(func)

if __name__ == "__main__":
    main()