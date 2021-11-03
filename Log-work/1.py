#Script Return the first line of the file

f1  = open("exam.log", "r")
txt = f1.read()
line1 = txt.split('\n')[0]
return line1