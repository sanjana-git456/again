nums = list(map(int, input("Enter: ").split()))
def ts(x):
    x = sorted(x)
    l = []
    for i in range(len(x)-1):
        if i > 0 and x[i] == x[i-1]:
            continue
        left = i+1
        right = len(x)-1
        fix = x[i]
        find = -fix
        while left < right:
            if x[left]+x[right] == find:
                l.append([x[i], x[left], x[right]])
                left += 1
                right -= 1
                while left < right and x[left] == x[left-1]:
                    left += 1
            elif x[left]+x[right] > find:
                right -= 1
            else:
                left += 1
    return l
print(ts(nums))