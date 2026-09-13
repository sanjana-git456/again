nums = input("Enter: ")
def ls(x):
    left = 0
    seen = set()
    maxlen = 0
    for right in range(len(x)):
        while x[right] in seen:
            seen.remove(x[left])
            left += 1
        seen.add(x[right])
        maxlen = max(maxlen, right-left+1)
    return maxlen
print(ls(nums))