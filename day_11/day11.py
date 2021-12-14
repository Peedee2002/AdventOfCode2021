class Octopuses():
    def __init__(self, octopusArray):
        self.octopusArray = [[(value, False) for value in row] for row in octopusArray]
        self.flashes = 0
    def inRange(self, x, y):
        return (0 <= x < len(self.octopusArray) and 0 <= y < len(self.octopusArray[0]))
    def flash(self, x, y):
        if not self.inRange(x, y):
            return
        self.flashes += 1
        self.octopusArray[x][y] =  (self.octopusArray[x][y][0], True)
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.inRange(i, j) and not self.octopusArray[i][j][1]:
                    self.octopusArray[i][j] = (self.octopusArray[i][j][0] + 1, self.octopusArray[i][j][1])

    def haveAllFlashed(self):
        for row in self.octopusArray:
            for value in row:
                if value[0] != 0:
                    return False
        return True

    def step(self):
        for x, row in enumerate(self.octopusArray):
            for y, value in enumerate(row):
                self.octopusArray[x][y] = (value[0] + 1, value[1])

        while True:
            hasCausedFlash = False
            for x, row in enumerate(self.octopusArray):
                for y, value in enumerate(row):
                    if value[0] > 9 and not value[1]:
                        self.flash(x, y)
                        hasCausedFlash = True
            if not hasCausedFlash:
                break

        for x, row in enumerate(self.octopusArray):
            for y, value in enumerate(row):
                if value[1]:
                    self.octopusArray[x][y] = (0, False)
        return self.haveAllFlashed()

if __name__ == '__main__':
    octopus = Octopuses([[int(c) for c in row[:-1]] for row in open('input.in')])
    for i in range(500):
        if octopus.step():
            print(f"we have flashed at step {i + 1}")
    print(f"there have been {octopus.flashes} flashes in total")
