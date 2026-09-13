x = list(map(int, input("Enter: ").split()))
def best(x):
    a = x[0]
    if len(x) == 1:
        return a
    b = max(a,x[1])
    for i in range(2,len(x)):
        c = max(b,a+x[i])
        a = b
        b = c
    return b
print(best(x))