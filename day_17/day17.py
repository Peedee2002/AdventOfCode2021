x_box = (244, 303)
y_box = (-91, -54)

def in_box(x, y):
    return x_box[0] <= x <= x_box[1] and y_box[0] <= y <= y_box[1]  

def simulate(vx, vy):
    x = 0
    y = 0
    landed = False
    heights = []
    while x <= x_box[1] and y >= y_box[0]:
        heights.append(y)
        x += vx
        y += vy
        vx -= 1 if vx > 0 else 0
        vy -= 1
        if in_box(x, y):
            landed = True
    return landed, max(heights)


if __name__ == '__main__':
    test_vx = range(x_box[1] + 1)
    # do as much as seems reasonable? this is dumb, but this is why engineering is better than science right
    # note: this is dumb because i have no guarantee on the upper bound here
    test_vy = range(y_box[0], (y_box[1] - y_box[0]) * 3)
    heights = []
    for vx in test_vx:
        for vy in test_vy:
            landed, height = simulate(vx, vy)
            if landed:
                heights.append(height)

    print(max(heights))
    print(len(heights))