import turtle

# Setup screen and turtle speed
turtle.speed(10)
turtle.pensize(2)

def draw_body():
    """Draw the bird's body as a filled gold circle."""
    turtle.penup()
    turtle.goto(0, -50)  # Move down so the bird is centered
    turtle.pendown()
    
    turtle.color("gold")
    turtle.begin_fill()
    turtle.circle(70)    # Using the built-in circle function
    turtle.end_fill()

def draw_beak():
    """Draw the bird's beak as a filled orange triangle."""
    turtle.penup()
    turtle.goto(65, 30)  # Move to the edge of the face
    turtle.pendown()
    turtle.right(30)
    
    turtle.color("darkorange")
    turtle.begin_fill()
    # 3 sides for the triangle
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    
    turtle.end_fill()
    turtle.right(120) # Reset turtle direction

def draw_eye():
    """Draw the bird's eye as a simple black dot."""
    turtle.penup()
    turtle.goto(25, 45)  # Position eye above the beak
    turtle.pendown()
    
    turtle.color("black")
    turtle.dot(15)       # dot() is perfect for drawing eyes without math

def draw_bird():
    """Draw the complete bird by combining the body, beak, and eye."""
    draw_body()
    draw_beak()
    draw_eye()

# Run the program
draw_bird()
turtle.hideturtle()
turtle.done()