import pgzrun

WIDTH = 800
HEIGHT = 400

def draw():
    screen.fill('white')
    screen.draw.filled_circle((400, 400), 300, 'red')
    screen.draw.filled_circle((400, 400), 250, 'orange')
    screen.draw.filled_circle((400, 400), 200, 'yellow')
    screen.draw.filled_circle((400, 400), 150, 'green')
    screen.draw.filled_circle((400, 400), 100, 'blue')
    screen.draw.filled_circle((400, 400), 50, 'cyan')
    screen.draw.filled_circle((400, 400), 25, 'purple')
    screen.draw.filled_circle((400, 400), 10, 'white')

pgzrun.go()