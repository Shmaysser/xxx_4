def countSquare(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def checkTriangle(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a

def reconfig(mass):
    newmass = []
    for object in mass:
        if (isinstance(object, float) or isinstance(object, int)) and object > 0:
            newmass.append(object)
    return newmass


digits = [1, 2, 3, 4, 5, 6, 'a', -1, -12241124, 'gesrhjsdgs']
digits = reconfig(digits)
digits.sort()
print(digits)
digits = digits[::-1]
mx = 0
for id1 in range(len(digits)):
    a = digits[id1]
    for id2 in range(id1 + 1, len(digits)):
        b = digits[id2]
        for id3 in range(id2 + 1, len(digits)):
            c = digits[id3]
            if checkTriangle(a, b, c):
                print(a, b, c)
                print(countSquare(a, b, c))
                exit()
if mx == 0:
    print('Треугольник существовать не может')
else:
    print(mx)