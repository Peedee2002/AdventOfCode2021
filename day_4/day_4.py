import numpy

class BingoCard():
    def __init__(self, cardInput) -> None:
        self.card = [[[value, 0] for value in row] for row in cardInput]
    def mark(self, number) -> None:
        for row in self.card:
            for value in row:
                if value[0] == number:
                    value[1] = 1

    def flatten(self: list[list[(int, int)]]) -> list[(int, int)]:
        return sum(self.card, [])
    def isWon(self) -> bool:
        transpose = numpy.transpose(self.card).tolist()
        actualTranspose = [list(zip(numberRow, valueRow)) for numberRow, valueRow in zip(transpose[0], transpose[1])]
                
        return any(BingoCard.isRowMarked(row) for row in self.card) \
            or any(BingoCard.isRowMarked(row) for row in actualTranspose)

    def isRowMarked(row) -> bool:
        return all([value[1] == 1 for value in row])

    def calculateScore(self, called) -> int:
        return sum(value[0] for value in self.flatten() if value[1] == 0) * called

if __name__ == '__main__':
    with open('input.in') as f:
        bingoNumbers = [int(number) for number in f.readline().split(",")]
        f.readline()
        bingoCards = []
        currentCard = []
        for line in f:
            if line.isspace():
                bingoCards.append(BingoCard(currentCard))
                currentCard.clear()
            else:
                currentCard.append([int(number) for number in line.split()])
        bingoCards.append(BingoCard(currentCard))
        for number in bingoNumbers:
            for card in bingoCards.copy():
                card.mark(number)
                if card.isWon():
                    print("winning card: " + str(card.calculateScore(number)))
                    bingoCards.remove(card)