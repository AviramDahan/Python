Polindrom = input("Please Enter Text: ")
Polindrom.lower()
if Polindrom == Polindrom[::-1]:
    print("OK")
else:
    print("NOT")