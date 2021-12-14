from typing import Set, Tuple


def fold_up(points: Set[Tuple[int, int]], value):
    fixers = [point for point in points if point[1] > value]
    moved_points = points.copy()
    for fixer in fixers:
        moved_points.add((fixer[0], value - (fixer[1] - value)))
        moved_points.remove(fixer)
    return moved_points

def fold_left(points, value):
    fixers = [point for point in points if point[0] > value]
    moved_points = points.copy()
    for fixer in fixers:
        moved_points.add((value - (fixer[0] - value), fixer[1]))
        moved_points.remove(fixer)
    return moved_points

def fold(points, fold):
    match fold:
        case ('x', value):
            return fold_left(points, value)
        case ('y', value):
            return fold_up(points, value)
    return points

if __name__ == '__main__':
    folds = []
    points = set()
    for line in open('input.in'):
        match (line.split(',')):
            case [x, y]:
                points.add((int(x), int(y)))
            case ['\n']:
                pass
            case [f]:
                axis, value = f.split('=')
                folds.append((axis[-1], int(value)))
    print(len(fold(points, folds[0])))
    curr = points
    for f in folds:
        curr = fold(curr, f)
    
    for i in range(6):
        for j in range(39):
            if (j, i) in curr:
                print('#', end='')
            else:
                print('-', end='')
        print()
    