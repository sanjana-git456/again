x = list(map(int, input("Enter: ").split()))
k = int(input("Enter: "))
def rotate(x,k):
    if k > len(x):
        k = k % len(x)
    l1 = []
    l2 = []
    l1 += x[-k:]
    l2 += x[:-k]
    return l1+l2
print(rotate(x,k))