# Day 22

def recursive_game(deck1, deck2):
    playedDecks = []

    while len(deck1) != 0 and len(deck2) != 0:
        if (deck1, deck2) in playedDecks:
            return 'p1'
        else:
            # pass a copy, not the new, popped decks!
            playedDecks.append((deck1.copy(), deck2.copy()))

            p1 = deck1.pop(0)
            p2 = deck2.pop(0)

            # get winner from a recursive game
            if len(deck1) >= p1 and len(deck2) >= p2:
                # the recursive game is played with shortened decks with different lengths!
                subDeck1 = deck1.copy()[0:p1]
                subDeck2 = deck2.copy()[0:p2]
                winner = recursive_game(subDeck1, subDeck2)

                if winner == 'p1':
                    deck1.append(p1)
                    deck1.append(p2)
                else:
                    deck2.append(p2)
                    deck2.append(p1)

            # get winner by card value
            else:
                if p1 > p2:
                    deck1.append(p1)
                    deck1.append(p2)
                elif p2 > p1:
                    deck2.append(p2)
                    deck2.append(p1)

    # check if game is over by not having cards
    if len(deck1) == 0:
        return 'p2'
    else:
        return 'p1'


if __name__ == '__main__':

    print(f"Part One")
    # Get Data
    data = []
    for line in open("puzzle_input.txt", 'r').readlines():
        line = line.strip('\n')
        if line == '':
            pass
        elif 'Player' in line:
            pass
        else:
            data.append(int(line))

    deck1 = data[0:(len(data) // 2)]
    deck2 = data[(len(data) // 2):]
    print("Deck 1", deck1)
    print("Deck 2", deck2)

    while len(deck1) != 0 and len(deck2) != 0:
        # draw one from each deck
        p1 = deck1.pop(0)
        p2 = deck2.pop(0)

        # compare
        if p1 > p2:
            deck1.append(p1)
            deck1.append(p2)
        else:
            deck2.append(p2)
            deck2.append(p1)

    print("Game Over!")
    if len(deck1) != 0:
        winningDeck = deck1
    else:
        winningDeck = deck2

    print("Winning Deck:", winningDeck)

    # Calculate Score
    score = 0
    for i in range(0, len(winningDeck)):
        score += winningDeck[i] * (len(winningDeck) - i)

    print("Score:", score)

    # Part Two
    print("Part Two")

    # Get Data
    data = []
    for line in open("puzzle_input.txt", 'r').readlines():
        line = line.strip('\n')
        if line == '':
            pass
        elif 'Player' in line:
            pass
        else:
            data.append(int(line))

    deck1 = data[0:(len(data) // 2)]
    deck2 = data[(len(data) // 2):]

    # get winner from recursive game
    winner = recursive_game(deck1, deck2)

    if winner == 'p1':
        winningDeck = deck1
    else:
        winningDeck = deck2

    print("Winning Deck:", winningDeck)
    # Calculate Score
    score = 0
    for i in range(0, len(winningDeck)):
        score += winningDeck[i] * (len(winningDeck) - i)

    print("Score:", score)
