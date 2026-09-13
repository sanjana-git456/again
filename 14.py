x = list(map(int, input("Enter: ").split()))
def best(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    a = x[0]
    b = max(a,x[1])
    for i in range(2,len(x)):
        c = max(b,a+x[i])
        a = b
        b = c
    return b
print(best(x))