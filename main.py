import turtle
import random

# A code to create randomly coloured drawings using turtle graphics.

def random_color(): 
    """Defines a function that returns a randomly generated colour in RGB format."""
    r = random.randint(0, 255)
    g = random.randint(0, 255) 
    b = random.randint(0, 255) 
    return (r, g, b)

# Ensure turtle can interpret rgb values 0-255
turtle.colormode(255) 

def draw_star(color, size, x, y):
    """Draw a star with a given size and color at (x, y)."""
    turtle.up() 
    turtle.goto(x, y) 
    turtle.down() 
    
    turtle.fillcolor(color)
    turtle.begin_fill() 
    
    for _ in range(5): 
        turtle.pencolor("black") 
        turtle.forward(size) 
        turtle.right(144) 
    
    turtle.end_fill() 

def draw_nested_stars(color, size, x, y, depth):
    """Draw a star and recursively draw smaller stars at each of its points."""
    if depth == 0: 
        return
    
    draw_star(color, size, x, y)
    
    # Recursive step: Draw smaller stars at each point of the current star
    for _ in range(5):
        # Move to the next point of the star
        turtle.forward(size)
        
        # Draw a smaller nested star at this position
        draw_nested_stars(random_color(), size / 2, turtle.xcor(), turtle.ycor(), depth - 1)
        
        # Move back to the previous position
        turtle.backward(size)
        
        # Rotate to the next point of the star
        turtle.right(144)

# Environment Setup and Cleanup
def setup_turtle_environment():
    turtle.speed(0)  
    turtle.bgcolor("lightblue")  
    turtle.hideturtle()  

def cleanup_turtle():
    turtle.done()  

# --- MAIN EXECUTION ---
# Set up the environment
setup_turtle_environment()

# Start the recursive drawing
draw_nested_stars(random_color(), 100, 0, 0, 3)

# Cleanup/Keep window open
cleanup_turtle()