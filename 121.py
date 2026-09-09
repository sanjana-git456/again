x = list(map(int, input("Enter: ").split()))
def profit(x):
    left = 0
    right = len(x)-1
    m = x[right] - x[left]
    while left < right:
        new = x[right] - x[left]
        m = min(m,new)
        left += 1
        right -= 1
    if m < 0:
        return 0
    else:
        return m
print(profit(x))