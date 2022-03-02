class Bug:
    def __init__(self, initialposition):
        self.initialposition = initialposition
        self.direction = "right"

    def turn(self):
        if self.direction == "right":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "right"

    def move(self):
        if self.direction == "right":
            self.initialposition += 1
        elif self.direction == "left":
            self.initialposition -= 1

    def position(self):
        return self.initialposition

    def direction(self):
        return '%s' % self.direction


ant = Bug(10)
ant.move()
ant.turn()
ant.move()
ant.move()
print ant.position()
print ant.direction
