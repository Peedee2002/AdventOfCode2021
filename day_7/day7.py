def findFuelCost(difference: int):
    difference = abs(difference)
    # return difference # for p1
    return int(difference * (difference + 1) / 2)
    

if __name__ == '__main__':
    with open("input.in") as f:
        ls = [int(num) for num in f.readline().split(',')]
    print(
        min(
            sum(findFuelCost(pos - num) for num in ls) for pos in range(min(ls), max(ls))
        )
    )
