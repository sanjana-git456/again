x = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))
def bin(x):
    left = 0
    right = len(x)-1
    for i in range(len(x)):
        mid = (left+right)//2
        if mid == t:
            return i
        elif mid < t:
            left = mid+1
        elif mid > t:
            right = mid-1
    return -1
print(bin(x))