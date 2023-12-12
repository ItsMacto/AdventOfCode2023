def star1():
    games = []
    total = 0
    with open("input.txt",) as fp:
        for line in fp:
           games.append(line.strip().split()[1:])
        for i in range(len(games[0])):
            sum = 0
            print(i)
            for time in range(int(games[0][i])):
                distance = time * (int(games[0][i]) - time)
                if distance > int(games[1][i]):
                    sum += 1
            if total == 0:
                total = sum
            else:
                total *= sum
    print(total)
    return total
    

# is slow, could use quadratic equation to solve faster 
def star2():
    time = ''
    distance = ''
    total = 0
    with open("input.txt",) as fp:
        game = fp.readlines()
        # for c in game[0]:
        #     if c.isnumeric():
        #         time += c
        # for c in game[1]:
        #     if c.isnumeric():
        #         distance += c
        # leaving old way for personal reference and learning
        time = int(''.join(filter(str.isdigit, game[0])))
        distance = int(''.join(filter(str.isdigit, game[1]))) 
        for t in range(int(time)):
            
            d = t * (int(time) - t)
            if d > int(distance):
                total += 1 
    return total
            
if __name__ == "__main__":
    print("Star 1: ", star1())
    print("Star 2: ", star2())
