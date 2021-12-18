x_box = (244, 303)
y_box = (-91, -54)
 
def simulate(vx, vy):
    x, y = 0, 0
    landed = False
    heights = []
    while x <= x_box[1] and y >= y_box[0]:
        heights.append(y)
        x , y = vx + x, vy + y 
        vx -= 1 if vx > 0 else 0
        vy -= 1
        landed = x_box[0] <= x <= x_box[1] and y_box[0] <= y <= y_box[1] if not landed else landed
    return landed, max(heights)


if __name__ == '__main__':
    heights = []
    for vx in range(x_box[1] + 1):
        # note: this is dumb because i have no maths to guarantee on the upper bound here
        for vy in range(y_box[0], (y_box[1] - y_box[0]) * 3):
            landed, height = simulate(vx, vy)
            if landed:
                heights.append(height)
    print(max(heights))
    print(len(heights))