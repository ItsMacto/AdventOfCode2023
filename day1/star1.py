sum = 0

with open ('input.txt') as fp:
    for line in fp:
        num1, num2 = -1, -1
        for c in line:
            if c.isnumeric():
                if num1 == -1:
                    num1 = c
                num2 = c
                num = num1 + num2
        sum += int(num)
        
print(sum)