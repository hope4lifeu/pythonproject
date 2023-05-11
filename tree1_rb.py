import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # fastest speed

# Define colors for rainbow
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Draw trunk of tree
t.color('brown')
t.pensize(20)
t.penup()
t.goto(0, -200)
t.pendown()
t.setheading(90)
t.forward(200)

# Draw leaves
for i in range(360):
    # Set color based on angle of leaf
    t.color(colors[i % len(colors)])
    t.forward(i/4)  # increase length of branch as i increases
    t.right(30)  # angle of branch

# Hide turtle
t.hideturtle()

# Keep window open until closed by user
turtle.done()
#this code is a project to display rainbow colored tree by me 