if __name__ == '__main__':
    total = 0
    for line in open('input.in'):
        displayed = line.split(' | ')[1].split()
        total += len([*filter(lambda d: len(d) in [2, 4, 3, 7], displayed)])
    print(total)