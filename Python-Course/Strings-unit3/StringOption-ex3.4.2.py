STRING = input("Please Enter String: ")
STRING_CHANGE = STRING[1:len(STRING)]
STRING_CHANGE = STRING_CHANGE.replace("d", "e")
print(STRING[0]+STRING_CHANGE)