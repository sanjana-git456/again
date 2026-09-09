x = input("Enter: ")
y = input("Enter: ")
def anag(x,y):
    d1 = {}
    d2 = {}
    if len(x) != len(y):
        return False
    for i in x:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for i in y:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
    return d1 == d2
print(anag(x,y))