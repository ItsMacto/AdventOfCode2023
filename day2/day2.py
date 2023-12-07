import re
def star1(bag):
    
    sum = 0
    with open("input.txt") as fp:
        maxShown = []
        
        for i, line in enumerate(fp):
            maxShown.append({})
            start = line.find(":")
            games = re.split(r",|;",line[start + 1:-1])
            
            
            for game in games:
                shown = game[1:].split(' ')
                # ['12', 'blue'] = shown
                maxShown[i][shown[1]] = max(maxShown[i].get(shown[1], 0),int(shown[0]))
                
            possible = True
            for color, val in maxShown[i].items():
                if val > bag.get(color, 0):
                    possible = False
            if possible == True:
                sum += i + 1
    return sum
    
def star2():
    
    sum = 0
    with open("input.txt") as fp:
        maxShown = []
        
        for i, line in enumerate(fp):
            maxShown.append({})
            start = line.find(":")
            games = re.split(r",|;",line[start + 1:-1])
            
            
            for game in games:
                shown = game[1:].split(' ')
                # ['12', 'blue'] = shown
                maxShown[i][shown[1]] = max(maxShown[i].get(shown[1], 0),int(shown[0]))
                
            product = 1
            for val in maxShown[i].values():
                product *= val
            sum += product
    return(sum)
        
        
# only 12 red cubes, 13 green cubes, and 14 blue cubes    
bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

if __name__ == "__main__":
    print("Star 1: ", star1(bag))
    print("Star 2: ",star2())