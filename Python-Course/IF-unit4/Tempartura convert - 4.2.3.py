
Temperature = input("Insert the temperature you would like to convert: ")

TempSet = float(Temperature[:-1])
NewFTemp = 0.0
NewCTemp = 0.0


if 'C' and 'c' == str(Temperature[-1:]):
    NewFTemp = TempSet * 1.8 + 32
    print(f'{NewFTemp}F')

elif 'F' and 'f' == str(Temperature[-1:]):
    NewCTemp = ((TempSet - 32)/1.8)
    print(f'{NewCTemp}C')