x = list(map(int, input("Enter: ").split()))
def romin(x):
    left = 0
    right = len(x)-1
    m = 0
    while left < right:
        mid = (left+right) // 2
        if right == left:
            return mid
        elif x[mid] > x[right]:
            left = mid+1
        else:
            right = mid
print(romin(x))