from math import gcd

def star1():
    with open("input.txt") as fp:
        instructions = fp.readline().strip()
        print(instructions)
        next(fp)
        map = {}
        
        for line in fp:
            line = line.split()
            
            map[line[0]] = (line[2][1:-1], line[3][:-1])

        current = 'AAA'
        steps = 0
        length = len(instructions)
        
        
        while current != 'ZZZ':
            instruction = instructions[steps % length]
            if instruction == 'L':
                current = map[current][0]
            else:
                current = map[current][1]
            steps += 1
                
        return steps



def star2():
    with open("input.txt") as fp:
        instructions = fp.readline().strip()
        print(instructions)
        next(fp)
        map = {}
        
        for line in fp:
            line = line.split()
            
            map[line[0]] = (line[2][1:-1], line[3][:-1])

        current = []
        for i in map.keys():
            if i[2] == 'A':
                current.append(i)

        steps = []
        length = len(instructions)
        
        for i in range(len(current)):
            steps.append(0)
            while current[i][2] != 'Z':
                instruction = instructions[steps[i] % length]
                if instruction == 'L':
                    current[i] = map[current[i]][0]
                else:
                    current[i] = map[current[i]][1]
                steps[i] += 1
        print(steps)
        lcm = 1
        
        for i in steps:
            lcm = lcm*i//gcd(lcm, i)
        return lcm
    
    
    # old brute force code. LCM works almost instantly
        # allEndZ = False 
                
        # while not allEndZ:
        #     allEndZ = True
        #     instruction = instructions[steps % length]
            
        #     for i in range(len(current)):
        #         if instruction == 'L':
        #             current[i] = map[current[i]][0]
        #         else:
        #             current[i] = map[current[i]][1]
        #         if current[i][2] != 'Z':
        #             allEndZ = False
        #     steps += 1
            


if __name__ == "__main__":
    # print(star1()) 
    print(star2())