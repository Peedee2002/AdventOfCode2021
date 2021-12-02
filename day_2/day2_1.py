depth = 0
width = 0
for line in open('input.in'):
    match line.split():
        case ["forward", value]:
            width += int(value)
        case ["up", value]:
            depth -= int(value)
        case ["down", value]:
            depth += int(value)

print(depth * width)
