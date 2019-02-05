import string
import difflib
file = open('strings.txt', 'r')
strings = file.readlines()
file.close()
letters = list(string.ascii_lowercase)
twos = 0
threes = 0
for String in strings:
    two = 0
    three = 0
    for letter in letters:
        count = String.count(letter)
        if count == 2:
            two = 1
        if count == 3:
            three = 1
    twos += two
    threes += three
    
print("Checksum = ", twos * threes)

for stringA in strings:
    for stringB in strings:
        diff = [li for li in difflib.ndiff(stringA, stringB) if li[0] != ' ']
        #print(len(diff))
        if len(diff) == 2:
            print("The two strings are " + stringA + ", and " + stringB)
        