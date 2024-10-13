import turtle  # Import the turtle graphics library
from random import randint  # Import randint for random positioning of the apple

# Class representing the Snake in the game
class Snake: 
    def __init__(self, x, y):
        # Initialize the snake's head as a turtle object
        self.head = turtle.Turtle() 
        self.head.color('white')  # Set head color to white
        self.head.shape("square")  # The shape of the head is a square
        self.head.speed(0)  # Speed of animation for the head (0 is fastest)
        self.head.goto(x, y)  # Position the head at the initial coordinates (x, y)
        self.head.penup()  # Prevent the head from drawing on the screen
        self.direction = "stop"  # Snake initially not moving
        self.old_direction = None  # Store the last direction (used for game logic)
        self.speed_of_snake = 15  # Initial movement speed of the snake
        self.max_speed = 20  # Maximum speed the snake can achieve
        self.body = []  # List to store body segments

    # Adds a new segment to the snake's body
    def add_segment(self):
        self.body.append(Segment())  # Append a new Segment object to the body list

    # Moves the head of the snake based on its current direction
    def head_move(self):
        if self.direction == "Up":
            # Move up by increasing the y-coordinate
            self.head.sety(self.head.ycor() + self.speed_of_snake)
        elif self.direction == "Down":
            # Move down by decreasing the y-coordinate
            self.head.sety(self.head.ycor() - self.speed_of_snake)
        elif self.direction == "Right":
            # Move right by increasing the x-coordinate
            self.head.setx(self.head.xcor() + self.speed_of_snake)
        elif self.direction == "Left":
            # Move left by decreasing the x-coordinate
            self.head.setx(self.head.xcor() - self.speed_of_snake)

    # Moves the body segments to follow the head
    def body_move(self):
        # Move the last segment to the position of the previous one
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].snake.showturtle()  # Ensure the segment is visible
            x = self.body[idx - 1].snake.xcor()  # Get the x-coordinate of the previous segment
            y = self.body[idx - 1].snake.ycor()  # Get the y-coordinate of the previous segment
            self.body[idx].snake.goto(x, y)  # Move the current segment to the previous one's position
        
        # If there's at least one segment, move the first segment to follow the head
        if len(self.body) != 0:
            self.body[0].snake.showturtle()  # Make sure the first body segment is visible
            self.body[0].snake.setx(self.head.xcor())  # Move to the head's x-coordinate
            self.body[0].snake.sety(self.head.ycor())  # Move to the head's y-coordinate

    # Check if the snake has hit the game boundaries
    def has_hit_boundaries(self):
        x = self.head.xcor()  # Get the x-coordinate of the head
        y = self.head.ycor()  # Get the y-coordinate of the head
        
        # Check if the head has crossed the game area boundaries
        if not (-395 < x < 395 and -295 < y < 295):
            self.speed_of_snake = 15  # Reset the speed of the snake
            self.direction = "stop"  # Stop the snake
            self.old_direction = "stop"  # Reset the last direction
            
            # Hide all body segments and delete them
            for segment in self.body:
                segment.snake.hideturtle()  # Hide the segment from the screen
                del segment.snake  # Delete the turtle object of the segment

            self.body.clear()  # Clear the body list
            self.head.goto(0, 0)  # Reset the head's position to the center
            
            # Return True indicating the snake has hit the boundary
            return True   
        
        # Return False if the snake hasn't hit any boundaries
        return False

    # Check if the snake has collided with itself
    def has_hit_itself(self):
        # Loop through each body segment
        for seg in self.body:
            # Check if the head is within a close distance to any segment (self-collision)
            if self.head.distance(seg.snake) < 10:
                self.speed_of_snake = 15  # Reset the speed of the snake
                self.direction = "stop"  # Stop the snake
                self.old_direction = "stop"  # Reset the last direction
                
                # Hide and delete all body segments
                for segment in self.body:
                    segment.snake.hideturtle()
                    del segment.snake
                
                self.body.clear()  # Clear the body list
                self.head.goto(0, 0)  # Reset the head's position to the center
                
                # Return True indicating a self-collision has occurred
                return True
        
        # Return False if no self-collision has occurred
        return False

    # String representation of the Snake object
    def __str__(self):
        return "self of Snake"

# Class representing a single body segment of the snake
class Segment:
    def __init__(self):
        # Initialize the segment as a turtle object
        self.snake = turtle.Turtle()  
        self.snake.color('green')  # Set segment color to green
        self.snake.penup()  # Prevent the segment from drawing on the screen
        self.snake.shape("square")  # Set the shape of the segment to square
        self.snake.speed(0)  # Fastest animation speed for the segment
        self.snake.hideturtle()  # Initially hide the segment

    # String representation of the Segment object
    def __str__(self):
        return "body of Snake"

# Class representing the Apple in the game
class Apple:
    def __init__(self):
        # Initialize the apple as a turtle object
        self.apple = turtle.Turtle()
        self.apple.color("red")  # Set apple color to red
        self.apple.penup()  # Prevent the apple from drawing on the screen
        self.apple.shape("circle")  # Set the shape of the apple to a circle
        self.apple.goto(150, 0)  # Position the apple at the initial location
        self.apple.speed(0)  # Fastest animation speed for the apple
        self.eaten_apples = 0  # Track the number of apples eaten

    # Move the apple to a new random location on the screen
    def move_apple(self):
        self.eaten_apples += 1  # Increment the count of eaten apples
        x = randint(-390, 390)  # Generate a random x-coordinate within the game boundaries
        y = randint(-290, 290)  # Generate a random y-coordinate within the game boundaries
        self.apple.setx(x)  # Move the apple to the new x-coordinate
        self.apple.sety(y)  # Move the apple to the new y-coordinate

# Class to display the score and other text on the screen
class Shown_text(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the turtle first
        self.color("White")  # Set the text color to white
        self.penup()  # Prevent the text turtle from drawing lines
        self.goto(0, 250)  # Position the text turtle at the top of the screen
        self.hideturtle()  # Hide the turtle (only the text is visible)
        self.speed(0)  # Fastest animation speed for the text turtle

    # Display the score on the screen
    def view_text(self, score):
        self.clear()  # Clear any previous text
        self.write(
            f"Score: {score}",  # Display the current score
            align="center",  # Center the text on the screen
            font=("Courier", 24, "normal")  # Set the font style and size
        )
