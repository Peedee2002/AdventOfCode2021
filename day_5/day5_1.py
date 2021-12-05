def rangeInclusive(beginning, end, reverse = False):
    values = range(beginning, end  + 1)
    return values if not reverse else reversed(values)

def interpolate_linear(beginning: tuple[int, int], end: tuple[int, int]):
    ''' interpolate all points between the beginning and end in a line'''
    if beginning[0] == end[0]:
        # horizontal
        return [(beginning[0], y) for y in rangeInclusive(*sorted([beginning[1], end[1]]))]
    elif beginning[1] == end[1]:
        # vertical
        return [(x, beginning[1]) for x in rangeInclusive(*sorted([beginning[0], end[0]]))]
    else:
        [beginning, end] = sorted([beginning, end])
        return zip(rangeInclusive(beginning[0], end[0]), rangeInclusive(*sorted([end[1], beginning[1]]), beginning[1] > end[1]))

if __name__ == '__main__':
    hypoMap = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in open('input.in'):
        tuples = [eval(tup) for tup in line.split(" -> ")]
        for x, y in interpolate_linear(tuples[0], tuples[1]):
            hypoMap[x][y] += 1
    
    print(sum([len([*filter(lambda a: a > 1, row)]) for row in hypoMap]))
