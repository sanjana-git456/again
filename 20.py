x = input("Enter: ")
def par(x):
    s = []
    d = {')':'(' , ']':'[' , '}':'{'}
    for i in x:
        if i not in d:
            s.append(i)
        else:
            if d[i] != s[-1]:
                return False
            s.pop()
    if s == []:
        return True
    else:
        return False
print(par(x))