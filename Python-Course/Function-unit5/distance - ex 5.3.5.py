def distance(num1, num2, num3):

    if (abs(num2-num1 or num3-num1) == 1) and (abs((num2-num1) + (num3-num2) or (num3-num2) + (num3-num1)) >= 2):
        print("TRUE")
    else:
        print("FALSE")

distance(num1=int(input("Num1: ")),num2=int(input("Num2: ")),num3=int(input("Num3: ")))