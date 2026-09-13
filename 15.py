nums = list(map(int, input("Enter: ").split()))
def ts(x):
    x = sorted(x)
    for i in range(len(x)-1):
        left = i+1
        right = len(x)-1
        fix = x[i]
        find = -fix
        while left < right:
            if x[left]+x[right] == find:
                return left, right, i
            elif x[left]+x[right] > find:
                right -= 1
            else:
                left += 1
print(ts(nums))