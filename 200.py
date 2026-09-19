grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def num(x):
    count = 0
    for r in range(len(x)):
        for c in range(len(x[0])):
            if x[r][c] == '1':
                count += 1
                island(x,r,c)
    return count

def island(x,r,c):
    if r < 0 or r >= len(x) or c < 0 or c >= len(x[0]) or x[r][c] != '1':
        return
    x[r][c] = 0
    island(x,r-1,c) #up
    island(x,r,c+1) #right
    island(x,r+1,c) #down
    island(x,r,c-1) #left

print(num(grid))