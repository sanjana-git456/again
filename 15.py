nums = list(map(int, input("Enter: ").split()))
target = int(input("Enter target: "))
def ts(x,t):
    left = 0
    right = len(x)
    for i in range(len(x)):
        fix = t - x[i]
        x = sorted(x)
        if x[left] + x[right] == fix:
            return left,right,i
        elif x[left] + x[right] > fix:
            right -= 1
        else:
            left += 1
    