# return the id of the fastest transaction

f1  = open("exam.log", "r")
txt = f1.read()
lines = txt.split('\n')
trans = {}


def toSecs(s): ##converst time to seconds (double)
    hr = int(s[:2])
    m = int(s[3:5])
    secs = float(s[6:])
    return secs + 60 * (m + 60*hr)

ctr2 = 0
for line in lines:
    desc = (line.split('\t')[4]).split(' ')
    if desc[0] == 'transaction' and desc[2] == 'begin':
        trans[desc[1]] = [(line.split('\t')[0]).split(' ')[1], "end", "dur"]
        ctr2 = ctr2 + 1

ctr = 0
for line in lines:
    desc = (line.split('\t')[4]).split(' ')
    if (line.split('\t')[4]).split(' ')[:2] == ['end', 'transaction']:
        tmp = trans[desc[2]]
        trans[desc[2]] = [tmp[0], (line.split('\t')[0]).split(' ')[1], "dur"]
        fastID = desc[2]
        ctr = ctr + 1

fastDur = toSecs(trans[fastID][1]) - toSecs(trans[fastID][0])

for ID in trans:
    trans[ID] = (trans[ID][:2]) + \
    [toSecs(trans[ID][1]) - toSecs(trans[ID][0])]
    if trans[ID][2] < fastDur:
        fastDur = trans[ID][2]
        fastID = ID

return fastID