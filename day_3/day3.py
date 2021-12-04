def flip(letter) -> str:
    return "0" if letter == "1" else "1"

def getMostCommon(index: int, lines: list[str]) -> str:
    thingo = [line[index] for line in lines]
    return "0" if thingo.count("0") > thingo.count("1") else "1"

def getQ2Thingo(lines: list[str], index: int, most: bool):
    if len(lines) == 1:
        return lines[0]
    mostCommon = getMostCommon(index, lines)
    filterBy =  mostCommon if most else flip(mostCommon)
    return getQ2Thingo([line for line in lines if line[index] == filterBy], index + 1, most)

if __name__ == '__main__':
    with open('input.in') as f:
        lines = f.readlines()
    o2 = int(getQ2Thingo(lines, 0, True), 2)
    Co2 = int(getQ2Thingo(lines, 0, False), 2)
    print(o2 * Co2)
