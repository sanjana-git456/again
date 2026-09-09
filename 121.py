x = list(map(int, input("Enter: ").split()))
def profit(x):
    minprice = x[0]
    maxprofit = 0
    for i in range(len(x)):
        diff = x[i]-minprice
        maxprofit = max(maxprofit,diff)
    if x[i] < minprice:
        minprice = x[i]
    return maxprofit
print(profit(x))