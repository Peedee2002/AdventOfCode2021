x_box, y_box = (244, 303), (-91, -54)
def simulate(vx, vy):
    x, y, landed, heights = 0, 0, False, []
    while x <= x_box[1] and y >= y_box[0]:
        heights.append(y)
        x , y, vx, vy = vx + x, vy + y, vx - 1 if vx > 0 else vx, vy - 1
        landed = x_box[0] <= x <= x_box[1] and y_box[0] <= y <= y_box[1] if not landed else landed
    return landed, max(heights)
heights = [simulate(vx, vy)[1] for vx in range(x_box[1] + 1) for vy in range(y_box[0], (y_box[1] - y_box[0]) * 3) if simulate(vx, vy)[0]]
print(max(heights), len(heights))
