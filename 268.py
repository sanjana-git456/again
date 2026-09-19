x = list(map(int, input("Enter: ").split()))
def missing(x):
    n = len(x)
    orig = n*(n+1)//2
    new = sum(x)
    m = orig-new
    return m
print(missing(x))