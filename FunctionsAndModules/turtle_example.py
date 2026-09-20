import turtle

# Setup screen and turtle speed
turtle.speed(3)
turtle.pensize(2)

# 1. Draw the Body (Circle)
def draw_body():
    turtle.penup()
    turtle.goto(0, -50)  # Move down so the bird is centered
    turtle.pendown()
    
    turtle.color("gold")
    turtle.begin_fill()
    turtle.circle(70)    # Using the built-in circle function
    turtle.end_fill()

# 2. Draw the Beak (Triangle using forward and turns)
def draw_beak():
    turtle.penup()
    turtle.goto(70, 20)  # Move to the edge of the face
    turtle.pendown()
    
    turtle.color("darkorange")
    turtle.begin_fill()
    turtle.right(50)
    # 3 sides for the triangle
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    
    turtle.end_fill()
    turtle.right(120) # Reset turtle direction

# 3. Draw the Eye (Simple dot)
def draw_eye():
    turtle.penup()
    turtle.goto(25, 45)  # Position eye above the beak
    turtle.pendown()
    
    turtle.color("black")
    turtle.dot(15)       # dot() is perfect for drawing eyes without math

# The main method that pieces the problem together
def draw_bird():
    draw_body()
    draw_beak()
    draw_eye()

# Run the program
draw_bird()
turtle.hideturtle()
turtle.done()