def func(num):
    # return num # for p1
    return int((num * (num + 1))/2)
    

if __name__ == '__main__':
    with open("input.in") as f:
        ls = [int(num) for num in f.readline().split(',')]
    print(
        min(
            sum(func(abs(pos - num)) for num in ls) for pos in range(min(ls), max(ls))
        )
    )
