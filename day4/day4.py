def star1():
    cards = []
    total = 0
    with open('input.txt') as fp:
        for line in fp:
            cards.append(line.strip().split())
        for card in cards:
            i = 2
            winningSet = set()
            matchs = 0
            while card[i] != '|':
                winningSet.add(card[i])
                i += 1
            while i < len(card):
                if card[i] in winningSet:
                    matchs += 1
                i += 1
            total += int(2**(matchs - 1))
    return(total)
            
def star2():
    cards = []
    total = 0
    with open('input.txt') as fp:
        for line in fp:
            cards.append(line.strip().split())
        cardMultiple = [1] * (len(cards))
        for j, card in enumerate(cards):
            i = 2
            winningSet = set()
            matchs = 0
            while card[i] != '|':
                winningSet.add(card[i])
                i += 1
            while i < len(card):
                if card[i] in winningSet:
                    matchs += 1
                i += 1
            for m in range(matchs):
                cardMultiple[j + m + 1] += 1 * cardMultiple[j]
            total = sum(cardMultiple)
    return(total)
            
if __name__ == "__main__":
    print("Star 1: ", star1())
    print("Star 2: ", star2())
