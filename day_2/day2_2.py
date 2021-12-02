depth = 0
width = 0
aim = 0
for line in open('input.in'):
    match line.split():
        case ["forward", value]:
            width += int(value)
            depth += aim * int(value)
        case ["up", value]:
            aim -= int(value)
        case ["down", value]:
            aim += int(value)

print(depth * width)
