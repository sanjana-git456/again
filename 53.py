x = list(map(int, input("Enter: ").split()))
def subsum(x):
    current = 0
    maxsum = x[0]
    for i in x:
        current += i
        maxsum = max(maxsum, current)
        if current < 0:
            current = 0
    return maxsum
print(subsum(x))