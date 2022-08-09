import turtle

t = turtle.Pen()
t.speed(1)
x = 40
len_side = 90
for m in range(3, 9):
    sum_interior_angle = (m-2)*180
    interior_angle = sum_interior_angle / m
    # t.penup()
    t.goto(x, 0)
    # t.pendown()
    t.left(180 - interior_angle/2)
    t.forward(len_side)
    for n in range(1, m):
        t.left(180 - interior_angle)
        t.forward(len_side)
    t.right(interior_angle/2)
    x += 1
