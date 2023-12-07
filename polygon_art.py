import turtle
import random

class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)
    
    def scale(self, reduction_ratio=0.618):
        turtle.penup()
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= reduction_ratio
        
    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

class Generate:
    def __init__(self, mode):
        self.mode = mode
        self.instruction = {1: [3, 0],
                            2: [4, 0],
                            3: [5, 0],
                            4: [random.randint(3, 5), 0],
                            5: [3, 2],
                            6: [4, 2],
                            7: [5, 2],
                            8: [random.randint(3,5), 2]}

    def generate(self):
        sides = self.instruction[self.mode][0]
        embed = self.instruction[self.mode][1]
        for i in range(20):
            p = Polygon(sides)
            p.draw()
            for j in range(embed):
                p.scale()
                p.draw()
                
# if __name__ == '__main__':
    # THE CODE BELOW IS FOR TESTING ONLY
    # You should run from run_polygon.py
    # turtle.speed(0)
    # turtle.bgcolor('black')
    # turtle.tracer(0)
    # turtle.colormode(255)
    # for i in range(20):
    #     p = Polygon(3)
    #     p.draw()
    #     p.scale(1)
    #     p.draw()
    # turtle.done()