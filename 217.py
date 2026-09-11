x = list(map(int, input("Enter: ").split()))
def dup(x):
    d = {}
    for i in x:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        if d[i] > 1:
            return True
    return False

def dup2(x):
    return len(set(x)) != len(x)

def dup3(x):
    seen = set()
    for i in x:
        if i in seen:
            return True
        seen.add(i)
    return False
print(dup(x))
print(dup2(x))
print(dup3(x))