import turtle
import random
from polygon_art import Polygon

class Generate:
    def __init__(self, mode):
        self.mode = mode
        self.instruction = {1: [3, 0],
                            2: [4, 0],
                            3: [5, 0],
                            4: [None, 0],
                            5: [3, 2],
                            6: [4, 2],
                            7: [5, 2],
                            8: [None, 2]}

    def generate(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        for i in range(20):
            sides = self.instruction[self.mode][0]
            embed = self.instruction[self.mode][1]
            if sides == None:
                sides = random.randint(3,5)
            p = Polygon(sides)
            p.draw()
            for j in range(embed):
                p.scale()
                p.draw()
        turtle.done()

if __name__ == '__main__':
    mode = int(input('Which art do you want to generate? Enter a number between 1 to 8, inclusive: '))
    g = Generate(mode)
    g.generate()