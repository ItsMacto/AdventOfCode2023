
def star1():
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
    return(sum)


def star2():
    sum = 0
    numbers = {
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
           }
    
    with open ('input.txt') as fp:
    # with open ('example2.txt') as fp:
        for line in fp:
            num1, num2 = -1, -1
            for i, c in enumerate(line):
                if c.isnumeric():
                    if num1 == -1:
                        num1 = c
                    num2 = c
                for n in numbers:
                    if line[i:].startswith(n):
                        if num1 == -1:
                            num1 = numbers[n]
                        num2 = numbers[n]
            num = num1 + num2
            sum += int(num)
    return(sum)



if __name__ == "__main__":
    print("Star 1: ", star1())  
    print("Star 2: ", star2())
