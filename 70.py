x = int(input("Enter: "))
def stairs(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    a = 1
    b = 2
    for i in range(3,x+1):
        c = a+b
        a = b
        b = c
    return b
print(stairs(x))