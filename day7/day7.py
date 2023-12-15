def handRank1(hand, starNum=1):
    value = ['AKQJT98765432']
    valueDict =  {v: i for i, v in enumerate(value[0])}
    count = {v: hand.count(v) for v in set(hand)}
    handValue = tuple(valueDict[v] for v in hand)
    countValue = sorted((v for v in count.values()), reverse=True)

    if 5 in countValue:        
        return (1,)  + handValue # Five of a kind
    if 4 in countValue:
        return (2, ) + handValue # Four of a kind
    elif 3 in countValue and 2 in countValue:
        return (3, ) + handValue # Full house
    elif 3 in countValue:
        return (4, ) + handValue # Three of a kind
    elif sorted(countValue) == [1, 2, 2]:
        return (5, ) + handValue # Two pair
    elif 2 in countValue:
        return (6, ) + handValue # Pair
    else:
        return (7,  ) + handValue # High card

def handRank2(hand, starNum=1):
    value = ['AKQT98765432J']
    valueDict =  {v: i for i, v in enumerate(value[0])}
    count = {v: hand.count(v) for v in set(hand)}
    handValue = tuple(valueDict[v] for v in hand)
    jCount = count.get('J', 0)
    countValue = sorted((v for k, v in count.items() if k != 'J'), reverse=True)
    if countValue:
        countValue[0] += jCount
    else:
        countValue = [jCount]
    if 5 in countValue:        
        return (1,)  + handValue # Five of a kind
    if 4 in countValue:
        return (2, ) + handValue # Four of a kind
    elif 3 in countValue and 2 in countValue:
        return (3, ) + handValue # Full house
    elif 3 in countValue:
        return (4, ) + handValue # Three of a kind
    elif sorted(countValue) == [1, 2, 2]:
        return (5, ) + handValue # Two pair
    elif 2 in countValue:
        return (6, ) + handValue # Pair
    else:
        return (7,  ) + handValue # High card
        
def star1():
    rounds = []
    total = 0
    with open("input.txt", "r") as fp:
        for line in fp:
            hand, bet = line.split()
            rounds.append((hand, bet))
        rounds.sort(key=lambda x: handRank1(x[0]), reverse=True)
        for i, round in enumerate(rounds):
            total += int(round[1]) * (i+1)
            
        return total

def star2():
    rounds = []
    total = 0
    with open("input.txt", "r") as fp:
        for line in fp:
            hand, bet = line.split()
            rounds.append((hand, bet))
        rounds.sort(key=lambda x: handRank2(x[0]), reverse=True)
        for i, round in enumerate(rounds):
            total += int(round[1]) * (i+1)
            
        return total
                    
if __name__ == "__main__":
    print(star1())
    print(star2())
