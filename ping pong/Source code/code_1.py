import turtle
from Madrab import Madrab
from Ball import Ball



# Pressed_keys  
keys = {
    'w' : False, 
    "s" : False ,
    "Up" : False ,
    "Down" : False 
}

# Functions to change state of Keys 

def key_down (key) : 
    keys[key] = True 

def key_up (key) : 
  keys[key] = False 

    




# Main program starts here
if __name__ == "__main__":

    # Initialize screen object
    wind = turtle.Screen()

    # Set the window title
    wind.title("Ping Pong By Abdo")

    # Set the background color of the window
    wind.bgcolor("black")

    # Set the size of the window to 800x600 pixels
    wind.setup(width=800, height=600)

    # Prevent the screen from updating automatically to improve performance
    wind.tracer(0)

    # Create two paddle objects (Madrabs) and a ball object
    madrab1 = Madrab()
    madrab2 = Madrab()
    ball = Ball()

    # Set the properties for the paddles
    madrab1.properties_of_shape(0, "square", "blue", (-350, 0), 5, 1)  # Blue paddle on the left
    madrab2.properties_of_shape(0, "square", "red", (350, 0), 5, 1)   # Red paddle on the right

    # Set the properties for the ball
    ball.properties_of_shape(0, "circle", "white", (0, 0))  # White ball in the center

    # Set up keyboard controls to move the paddles
    wind.listen()  # Listen for key pressess


    wind.onkeypress(lambda : key_down('w') , 'w' )
    wind.onkeypress(lambda : key_down('s') , 's' )
    wind.onkeypress(lambda : key_down('Up') , 'Up' )
    wind.onkeypress(lambda : key_down('Down') , 'Down' )

    wind.onkeyrelease(lambda : key_up('w') , 'w' )
    wind.onkeyrelease(lambda : key_up('s') , 's' )
    wind.onkeyrelease(lambda : key_up('Up') , 'Up' )
    wind.onkeyrelease(lambda : key_up('Down') , 'Down' )






    # Main game loop
    while True:
        
        # Handle continuous movement of the Madrab 
        if keys['s'] : 
            madrab1.shape_move_down()
        if keys['w'] : 
            madrab1.shape_move_up()
        if keys['Up'] : 
            madrab2.shape_move_up()
        if keys['Down'] : 
            madrab2.shape_move_down()

        # Move the ball diagonally up and down
        check = ball.Diagonal_movement_up()
        check = ball.Diagonal_movement_down()

        # Detect if the ball hits either paddle
        ball.detect_madrab_hit(
            madrab1_x=madrab1.shape.xcor(), madrab1_y=madrab1.shape.ycor(),
            madrab2_x=madrab2.shape.xcor(), madrab2_y=madrab2.shape.ycor()
        )

        # Check if any player has lost the game (i.e., if the ball crosses either side)
        ball.check_player_loss()

        # Update the window with all the changes (paddles moving, ball movement, etc.)
        wind.update()
