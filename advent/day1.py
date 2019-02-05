file = open('numbers.txt', 'r')
lines = file.readlines()
changes = []
for line in lines:
    changes.append(int(line))
freq = 0
freqSet = set([0])
duplicate = False
while not duplicate:
    for change in changes:
        freq += change
        if freq in freqSet and not duplicate:
            print("Double Freq:" + str(freq))
            duplicate = True
        else:
            freqSet.add(freq)
file.close()