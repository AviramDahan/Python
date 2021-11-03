f1 = open ( "exam.log", "r" )
txt = f1.read ()
lines = txt.split ( '\n' )
ctr = 0
for line in lines:
    if (line.split ( '\t' )[4]).split ( ' ' )[:2] == ['end', 'transaction']:
        ctr = ctr + 1

ctr2 = 0
for line in lines:
    desc = (line.split ( '\t' )[4]).split ( ' ' )
    if desc[0] == 'transaction' and desc[2] == 'begin':
        ctr2 = ctr2 + 1

if ctr2 == ctr:
    return ctr