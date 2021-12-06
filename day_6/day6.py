from typing import Counter


DAYS = 256

if __name__ == '__main__':
    with open('input.in') as f:
        counter = Counter([int(number) for number in f.readline().split(',')])
    for _ in range(DAYS):
        counter = {
            0: counter[1],
            1: counter[2],
            2: counter[3],
            3: counter[4],
            4: counter[5],
            5: counter[6],
            6: counter[7] + counter[0],
            7: counter[8],
            8: counter[0]
        }
    print(sum(counter.values()))
