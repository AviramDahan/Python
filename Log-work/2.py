# Script to find log level ERROR in file

f1  = open("exam.log", "r")
txt = f1.read()
lines = txt.split('\n')
ctr = 0
for line in lines:
    if line.split('\t')[1] == 'ERROR':
        ctr = ctr + 1


return ctr