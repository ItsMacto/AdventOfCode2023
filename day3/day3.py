def checkAdjacent(x, y, l, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1),(0,1),(0,-1)]
    for i in range(l):
        xOffset = x + i
        for direction in directions:
            dx, dy = direction
            cx, cy = dx + xOffset, dy + y
            
            if (0<= cy < len(grid) and 0 <= cx < len(grid[cy])):
                if ((not grid[cy][cx].isnumeric()) and grid[cy][cx] != '.'):
                    return True
    return False
        
        
def star1():
    sum = 0
    grid = []
    with open('input.txt') as fp:
        for line in fp:
            grid.append(list(line.strip()))
            
        for y, line in enumerate(grid):
            x = 0
            while x < len(line):
                if line[x].isnumeric():
                    num = ''
                    start_x = x
                    while x < len(line) and line[x].isnumeric():
                        num += line[x]
                        x += 1
                    l = len(num) 
                    if checkAdjacent(start_x, y, l, grid):
                        sum += int(num)
                        
                x += 1
    return sum
                


print(star1())
