
def star1():
    with open('input.txt') as fp:
        data =[line.strip() for line in fp.readlines()]

        step = 0
        for i in range(len(data)):
            index = i + step
            if '#' not in data[index]:
                data.insert(index, '.' * len(data[index]))
                step += 1
                
        step = 0
        for i in range(len(data[0])):
            index = i + step 
            if '#' not in [line[index] for line in data]:
                for j in range(len(data)):
                    data[j] = data[j][:index] + '.' + data[j][index:]
                step += 1
            
    galaxies = []
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                galaxies.append((i, j))
                
                
    length = 0 
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            length += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
    
    
    return length


def star2():
    with open('input.txt') as fp:
        data =[line.strip() for line in fp.readlines()]
        rows = []
        for i in range(len(data)):
            if '#' not in data[i]:
                rows.append(i)
        
        columns = [] 
        for i in range(len(data[0])):
            if '#' not in [line[i] for line in data]:
                columns.append(i)
                
                
    galaxies = []
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                galaxies.append((i, j))
                
                
    length = 0
    
    
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            upperRow, lowerRow = max(galaxies[i][0], galaxies[j][0]), min(galaxies[i][0], galaxies[j][0])
            upperColumn, lowerColumn = max(galaxies[i][1], galaxies[j][1]), min(galaxies[i][1], galaxies[j][1])
            
            
            count = sum(lowerColumn <= column <= upperColumn for column in columns)
            count += sum(lowerRow <= row <= upperRow for row in rows)
            
            length += (abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]) + (count * 1_000_000 - count))
    
    return length



if __name__ == '__main__':
    print(star1())
    print(star2())