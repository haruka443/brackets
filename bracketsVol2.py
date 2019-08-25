sentence = 'Ala ma <kota>, a <kot> ma Alę'
toCount = False
amountOfSigns = 0

for letter in sentence:
    if letter == '>':
        toCount = False
    elif toCount:
        amountOfSigns += 1
    if letter == '<':
        toCount = True

print(f' Between <> are {amountOfSigns} signs')