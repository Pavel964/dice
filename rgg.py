import turtle as t
import math

t.color("red")
t.shape("turtle")
t.speed(5)

# договор
walls_width = 199
walls_height = 99
walls_color = "black"
door_width = 40
door_height = 70
door_color = "brown"
roof_side = math.sqrt(door_height ** 2 + (walls_width / 2) ** 2)
roof_angle = math.degrees(math.atan(door_height / (walls_width / 2)))
roof_color = "red"

# стены
t.fillcolor(walls_color)
t.begin_fill()
for i in range(2):
    t.fd(walls_width)
    t.left(90)
    t.fd(walls_height)
    t.left(90)
t.end_fill()

# двери
t.fd(walls_width / 2 - door_width / 2)
t.fillcolor(door_color)
t.begin_fill()
for i in range(2):
    t.fd(door_width)
    t.left(90)
    t.fd(door_height)
    t.left(90)
t.end_fill()

# крыша
t.right(180)
t.fd(walls_width / 2 - door_width / 2)
t.right(90)
t.fd(walls_height)
t.fillcolor(roof_color)
t.begin_fill()
t.right(90)
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle * 2)
t.fd(roof_side)
t.setheading(180)
t.fd(walls_width)
t.end_fill()

t.done()
