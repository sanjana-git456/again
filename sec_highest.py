x = list(map(int, input("Enter: ").split()))
def sechighest(x):
    if x[0] > x[1]:
        m1 = x[0]
        m2 = x[1]
    else:
        m1 = x[1]
        m2 = x[0]
    for i in x:
        if i > m1:
            m1 = i
            m2 = m1
        elif i < m1 and i > m2:
            m2 = i
    return m2
print(sechighest(x))