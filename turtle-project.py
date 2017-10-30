from turtle import *
blob = Turtle()
bleb = Turtle()
turtle = Turtle()
blob.shape("turtle")
bleb.shape("turtle")
colormode(255)
setup(1350,768)
Screen()
bleb.speed(20)
blob.speed(20)



def draw_star(t, x, y, points, line, fill):
    t.penup()
    t.goto(x, y)
    t.pendown()

    angle = 180 - (360 / points)

    t.color(line, fill)
    t.begin_fill()
    for i in range(points):
        t.forward(200)
        t.left(angle)
    t.end_fill()


bgcolor(255, 255, 255)
draw_star(blob, 200, 0, 6, ( 0, 0, 255) , (255, 255, 255))
blob.penup()
blob.left(90)
blob.forward(100)
blob.right(90)
blob.pendown()
blob.begin_fill()
blob.forward(200)
blob.right(120)
blob.forward(200)
blob.right(120)
blob.forward(200)
blob.right(120)
blob.forward(200)
blob.end_fill()

def draw_tunnel(t, x, y, size, line, fill):
    t.color(line, fill)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(x,y):
        t.circle(size)
    t.end_fill()

size = 50
speed(50)
while size < 200:
    draw_tunnel(bleb, 0, 0, 50, (0, 0, 0), (255, 255, 255))
    bleb.circle(size)
    size += 15

while size < 400:
    draw_tunnel(blob, -200, -200, 15, (0, 0, 0), (255, 255, 255))
    blob.circle(size)
    size += 15

draw_star(blob, -300, -75, 30, ( 255, 0, 0) , (0, 0, 255))


move = Turtle()
showturtle()
def k1():
    global moves
    
    if moves <= 42:
        move.forward(45)
        moves += 1
        
    

def k2():
    global moves
    
    if moves <= 42:
        move.left(45)
        moves += 1

def k3():
    global moves
    
    if moves <= 42:
        move.right(45)
        moves += 1

def k4():
    global moves
    
    if moves <= 42:
        move.back(45)
        moves += 1

moves = 0
onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")
listen()
mainloop()

