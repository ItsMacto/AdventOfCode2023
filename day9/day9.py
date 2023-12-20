from collections import deque

def star1():
    with open('input.txt') as fp:
    # with open('example.txt') as fp:
        data = [[int(item) for item in line.split()] for line in fp.read().splitlines()]
    
    total = 0
    for entry in data:
        predation = [entry]
        i = 0
        while not all (x == 0 for x in predation[i]):
            predation.append([])
            for j in range(len(predation[i]) - 1):
                predation[i + 1].append(predation[i][j + 1] - predation[i][j])
            i += 1
        predation[len(predation) - 1].append(0)
        for row in range(len(predation) - 2, -1, -1):
            predation[row].append(predation[row + 1][-1] + predation[row][-1])
                
        total += (predation[0][-1])
    return total

 
def star2():
    with open('input.txt') as fp:
    # with open('example.txt') as fp:
        data = [[int(item) for item in line.split()] for line in fp.read().splitlines()]
    
    total = 0
    for entry in data:
        predation = [deque(entry)]
        i = 0
        while not all (x == 0 for x in predation[i]):
            predation.append(deque())
            for j in range(len(predation[i]) - 1):
                predation[i + 1].append(predation[i][j + 1] - predation[i][j])
            i += 1
        predation[len(predation) - 1].appendleft(0)
        for row in range(len(predation) - 2, -1, -1):
            predation[row].appendleft(predation[row][0] -  predation[row + 1][0])
                
        total += (predation[0][0])
    return total
         
    
if __name__ == '__main__':
    print(star1())
    print(star2())