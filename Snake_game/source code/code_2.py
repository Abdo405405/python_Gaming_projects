from math import sqrt  # Import sqrt for distance calculations
import turtle  # Import turtle graphics library
from random import randint  # Import randint for random positioning of the apple
from snake import Snake, Apple  # Import Snake and Apple classes from the snake module
from time import sleep  # Import sleep for adding delays in the game loop
from snake import Shown_text  # Import Shown_text class for displaying score
from snake import make_sound
# Setup the game screen
win = turtle.Screen()  # Create a screen object
win.setup(width=800, height=600)  # Set the screen size to 800x600 pixels
win.bgcolor('black')  # Set the background color of the screen to black
win.title("Snake Game By Abdo")  # Set the title of the game window
win.tracer(0)  # Disable automatic screen updates for better control over rendering

# Setup game objects
snake = Snake(0, 0)  # Create a snake object with the head starting at coordinates (0, 0)
apple = Apple()  # Create an apple object
score = Shown_text()  # Create a text object to display the score

# Functions to control the snake's direction

def direc_up():
    # Change direction to up, but only if the current direction is not down
    snake.direction = "Up" if snake.old_direction != "Down" else "Down"
    snake.old_direction = snake.direction  # Update the old direction to the current one

def direc_down():
    # Change direction to down, but only if the current direction is not up
    snake.direction = "Down" if snake.old_direction != "Up" else "Up"
    snake.old_direction = snake.direction  # Update the old direction to the current one

def direc_left():
    # Change direction to left, but only if the current direction is not right
    snake.direction = "Left" if snake.old_direction != "Right" else "Right"
    snake.old_direction = snake.direction  # Update the old direction to the current one

def direc_right():
    # Change direction to right, but only if the current direction is not left
    snake.direction = "Right" if snake.old_direction != "Left" else "Left"
    snake.old_direction = snake.direction  # Update the old direction to the current one

# Function to check if the snake's head has touched the apple
def check_if_snake_and_apple_touched(x_square, y_square, x_circ, y_circ, square_side, circle_radius):
    # Calculate the Euclidean distance between the centers of the square (snake) and circle (apple)
    len_between_points = sqrt((x_square - x_circ) ** 2 + (y_circ - y_square) ** 2)

    # Calculate half of the diagonal of the square (distance from the center of the square to a corner)
    half_diagonal_square = square_side * sqrt(2) / 2

    # Check if the distance between the centers is less than or equal to the sum of the half diagonal and circle radius
    are_touching = len_between_points <= (half_diagonal_square + circle_radius)

    return are_touching  # Return True if they are touching, False otherwise

# Setup keyboard listeners
win.listen()  # Set up the screen to listen for keyboard inputs

# Map arrow key presses to the direction functions
win.onkeypress(direc_up, 'Up')  # When the "Up" arrow is pressed, call the direc_up function
win.onkeypress(direc_down, 'Down')  # When the "Down" arrow is pressed, call the direc_down function
win.onkeypress(direc_right, 'Right')  # When the "Right" arrow is pressed, call the direc_right function
win.onkeypress(direc_left, 'Left')  # When the "Left" arrow is pressed, call the direc_left function

# Main game loop
while True:
    # Display the current score on the screen
    score.view_text(apple.eaten_apples)
    
    # Move the snake's body and head
    snake.body_move()
    snake.head_move()

    # Add a delay to control the speed of the game
    sleep(0.09)

    # Check if the snake has touched the apple
    if check_if_snake_and_apple_touched(
        x_square=snake.head.xcor(), y_square=snake.head.ycor(),
        x_circ=apple.apple.xcor(), y_circ=apple.apple.ycor(),
        square_side=15, circle_radius=15
    ):
        
        apple.move_apple()  # Move the apple to a new random location
        # Increase the snake's speed after every 5 apples eaten, but not exceeding the max speed
        if not apple.eaten_apples % 5 and snake.speed_of_snake <= snake.max_speed:
            snake.speed_of_snake += 1  # Increase the snake's speed by 1

        snake.add_segment()  # Add a new segment to the snake's body

    # Check if the snake has hit the boundaries or itself
    if snake.has_hit_boundaries() or snake.has_hit_itself():
        apple.eaten_apples = 0  # Reset the score if the snake dies
        make_sound("game-start.mp3")
        

    # Update the screen with the latest changes
    win.update()
