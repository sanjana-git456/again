x = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))
def bin(x):
    left = 0
    right = len(x)-1
    while left <= right:
        mid = (left+right)//2
        if x[mid] == t:
            return mid
        elif x[mid] < t:
            left = mid+1
        elif x[mid] > t:
            right = mid-1
    return -1
print(bin(x))