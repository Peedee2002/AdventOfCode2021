x_box, y_box = (244, 303), (-91, -54)
def simulate(vx, vy):
    x, y, landed, max_h = 0, 0, False, 0
    while x <= x_box[1] and y >= y_box[0]:
        max_h, x , y, vx, vy, landed = max_h if y < max_h else y, vx + x, vy + y, vx - 1 if vx > 0 else vx, vy - 1, x_box[0] <= x <= x_box[1] and y_box[0] <= y <= y_box[1] if not landed else landed
    return landed, max_h
heights = [simulate(vx, vy)[1] for vx in range(x_box[1] + 1) for vy in range(y_box[0], (y_box[1] - y_box[0]) * 3) if simulate(vx, vy)[0]]
print(max(heights), len(heights))
