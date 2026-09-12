x = input("Enter: ").split()
def anag(x):
    d = {}
    for i in x:
        key = ''.join(sorted(i))
        if key in d:
            d[key].append(i)
        else:
            d[key] = [i]
    return d
print(anag(x))