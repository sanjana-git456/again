x = list(map(int, input("Enter: ").split()))
k = int(input("Enter k: "))
def freq(x,k):
    d = {}
    for i in x:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    l = []
    l.append(sorted(d.values))
    a = []
    for i in range(k):
        a.append(l[i])
    return a
print(freq(x,k))