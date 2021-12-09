from math import prod

def recursive_fill_basins(x, y, array):
    if array[x][y][0] == 9 or array[x][y][1]:
        return 0
    array[x][y] = (array[x][y][0], True)
    total = 0
    if  x - 1 >= 0:
        total += recursive_fill_basins(x - 1, y, array)
    if x + 1 < len(array):
        total += recursive_fill_basins(x + 1, y, array)
    if  y - 1 >= 0:
        total += recursive_fill_basins(x, y - 1, array)
    if y + 1 < len(array[0]):
        total += recursive_fill_basins(x, y + 1, array)
    return 1 + total

if __name__ == '__main__':
    array = [[(int(value), False) for value in line[:-1]] for line in open('example.in')]
    totals = [recursive_fill_basins(x, y, array) for x in range(len(array)) for y in range(len(array[0]))]

    print(prod(sorted(totals)[-3:]))