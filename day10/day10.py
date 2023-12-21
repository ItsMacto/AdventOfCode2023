



def star1():
    
    
    with open("input.txt") as fp:
    # with open("example.txt") as fp:
        field = fp.readlines()
    
    for y, line in enumerate(field):
        for x, char in enumerate(line):
            if char == 'S':
                start = (x, y)
                break
    
    x, y, steps = start[0], start[1], 0
    if x < len(field[0]) - 1 and field[y][x + 1] in ('-', '7', 'J'):
        move = (1, 0)
    elif y < len(field) - 1 and field[y + 1][x] in ('|', 'L', 'J'):
        move = (0, 1)
    elif x > 0 and field[y][x - 1] in ('-', 'F', 'L'):
        move = (-1, 0)
    elif y > 0 and field[y - 1][x] in ('|', 'F', '7'):
        move = (0, -1)
    
    
    x, y = x + move[0], y + move[1]

    while (x, y) != start:
        steps += 1
        if field[y][x] == "F":
            if move == (-1, 0):
                move = (0, 1)
            else:
                move = (1, 0)
        elif field[y][x] == "L":
            if move == (0, 1):
                move = (1, 0)
            else:
                move = (0, -1)
        elif field[y][x] == "7":
            if move == (1, 0):
                move = (0, 1)
            else:
                move = (-1, 0)
        elif field[y][x] == "J":
            if move == (0, 1):
                move = (-1, 0)
            else:
                move = (0, -1)
        x, y = x + move[0], y + move[1]
        
    return (steps + 1) // 2
   

def star2():
    
    
    with open("input.txt") as fp:
    # with open("example.txt") as fp:
        field =[line.strip() for line in fp.readlines()]
    
    map = [[0 for _ in row] for row in field]

    for y, line in enumerate(field):
        for x, char in enumerate(line):
            if char == 'S':
                start = (x, y)
                break
    
    x, y, steps = start[0], start[1], 0
    if x < len(field[0]) - 1 and field[y][x + 1] in ('-', '7', 'J'):
        move = (1, 0)
    elif y < len(field) - 1 and field[y + 1][x] in ('|', 'L', 'J'):
        move = (0, 1)
    elif x > 0 and field[y][x - 1] in ('-', 'F', 'L'):
        move = (-1, 0)
    elif y > 0 and field[y - 1][x] in ('|', 'F', '7'):
        move = (0, -1)
    
    map[y][x] = 1
    x, y = x + move[0], y + move[1]

    while (x, y) != start:
        map[y][x] = 1
        steps += 1
        if field[y][x] == "F":
            if move == (-1, 0):
                move = (0, 1)
            else:
                move = (1, 0)
        elif field[y][x] == "L":
            if move == (0, 1):
                move = (1, 0)
            else:
                move = (0, -1)
        elif field[y][x] == "7":
            if move == (1, 0):
                move = (0, 1)
            else:
                move = (-1, 0)
        elif field[y][x] == "J":
            if move == (0, 1):
                move = (-1, 0)
            else:
                move = (0, -1)
        x, y = x + move[0], y + move[1]
    
    
    # can make faster with hashmap 
    size = 0
    for i in range(len(map)):
        within = False
        for j in range(len(map[0])):
            if map[i][j] == 1:
                if field[i][j] in ['|', 'L', 'J']:
                    within = not within
            elif within:
                size += 1
    print(size)
            

if __name__ == '__main__':
    # print(star1())
    print(star2())