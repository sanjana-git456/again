x = list(map(int, input("Enter: ").split()))
k = int(input("Enter k: "))
def freq(x,k):
    d = {}
    for i in x:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    s = sorted(d.items(), key = lambda x:x[1],reverse = True)
    return s
print(freq(x,k))