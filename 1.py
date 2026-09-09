x = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))
def ts(x,t):
    d = {}
    for i in range(len(x)):
        a = t-x[i]
        if a in d:
            return d[a],i
        d[x[i]] = i
    return -1
print(ts(x,t))