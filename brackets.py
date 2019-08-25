writing = 'Ala ma <kota>, a kot ma Alę'
startPosition = None
endPosition = None

for position, letter in enumerate(writing):
    if letter == '<':
        startPosition = position
    elif letter == '>':
        endPosition = position - 1
        break

print(f'Between <> are {endPosition - startPosition} signs')
