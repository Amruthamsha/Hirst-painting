#import colorgram
import turtle as t
import random

tom = t.Turtle()
#tom.shape("turtle")


#rgb_colors = []
#colors = colorgram.extract('hirst.jpeg', 10)
#print(colors)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#
#print(rgb_colors)
tom.speed("fastest")
t.colormode(255)
color_list = [(189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (208, 211, 208), (211, 209, 210),
              (64, 43, 43), (171, 183, 170)]
tom.penup()
tom.setheading(225)
tom.forward(350)
tom.setheading(0)
no_of_dots = 100

for dot_count in range(1, no_of_dots+1):
    tom.dot(20, random.choice(color_list))
    tom.penup()
    tom.forward(50)
    tom.pendown()

    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.penup()
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)

screen = t.Screen()
screen.exitonclick()