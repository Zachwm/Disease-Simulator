# Each person in the simulation
class Person:
    RADIUS = 10

    def __init__(self, canvas, x, y, dx, dy, infected=False):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.state = 'red' if infected else 'white'
        self.id = canvas.create_oval(
            x - self.RADIUS, y - self.RADIUS, x + self.RADIUS, y + self.RADIUS,
            fill=self.state
        )
        
    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x - self.RADIUS < 0 or self.x + self.RADIUS > 1280:
            self.dx *= -1
        if self.y - self.RADIUS < 0 or self.y + self.RADIUS > 720:
            self.dy *= -1

        self.canvas.move(self.id, self.dx, self.dy)

    def update_color(self, color):
        self.state = color
        self.canvas.itemconfig(self.id, fill=color)

    def get_color(self):
        return self.canvas.itemcget(self.id, 'fill')
