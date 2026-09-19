x = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))
def find(x,t):
    left = 0
    right = len(x)-1
    while left <= right:
        mid = (left+right)//2
        if x[mid] == t:
            return mid
        if x[left] <= x[mid]:
            if x[left] <= t < x[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if x[mid] <= t < x[right]:
                left = mid+1
            else:
                right = mid-1
    return -1
print(find(x))