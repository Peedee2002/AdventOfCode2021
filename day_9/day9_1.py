def somethingLower(x: int, y: int, value: int, array: list[list[int]]):
    return (x - 1 >= 0 and array[x - 1][y] <= value) or (x + 1 < len(array) and array[x + 1][y] <= value) \
    or (y - 1 >= 0 and array[x][y - 1] <= value) or (y + 1 < len(array[0]) and array[x][y + 1] < value)

if __name__ == '__main__':
    array = [[int(value) for value in line[:-1]] for line in open('example.in')]
    answer = 0
    for x, row in enumerate(array):
        for y, value in enumerate(row):
            if not somethingLower(x, y, value, array):
                answer = answer + 1 + value
    print(answer)
