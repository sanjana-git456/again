x = list(map(int, input("Enter: ").split()))
def dup(x):
    d = {}
    for i in x:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        if d[i] == 1:
            return False
        else:
            return True
print(dup(x))