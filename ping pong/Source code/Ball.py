from Shape import Shape
from Score import Score

# Ball class inherits from Shape
class Ball(Shape):
    def __init__(self):
        # Set initial movement direction for x and y (dx, dy)
        self.dx = 0.15
        self.dy = 0.15
        
        # A flag to determine which side (left or right) is currently active
        self.flag = 0
        
        # Initialize player scores for player 1 and player 2
        self.score_of_p1 = 0
        self.score_of_p2 = 0
        
        # Create a Score object to handle the display of the score
        self.score = Score()

        # Call the parent class (Shape) constructor to initialize the ball as a shape
        super().__init__()

    # Method to move the ball diagonally upwards
    def Diagonal_movement_up(self):
        # Get current x and y coordinates of the ball (rounded for precision)
        x = round(self.shape.xcor(), 5)
        y = round(self.shape.ycor(), 5)

        # If the ball reaches the top boundary (y > 275), reverse its vertical direction
        if 0 < y > 275:
            self.shape.sety(275)  # Prevent the ball from going off the screen
            self.dy *= -1         # Reverse the direction of the ball's y movement
        else:
            # Continue moving the ball diagonally by updating x and y positions
            self.shape.sety(y + round(self.dy, 5))
            self.shape.setx(x + round(self.dx, 5))

    # Method to move the ball diagonally downwards
    def Diagonal_movement_down(self):
        # Get current x and y coordinates of the ball (rounded for precision)
        x = round(self.shape.xcor(), 5)
        y = round(self.shape.ycor(), 5)

        # If the ball reaches the bottom boundary (y < -275), reverse its vertical direction
        if 0 > y < -275:
            self.shape.sety(-275)  # Prevent the ball from going off the screen
            self.dy *= -1          # Reverse the direction of the ball's y movement
        else:
            # Continue moving the ball diagonally by updating x and y positions
            self.shape.sety(y + round(self.dy, 5))
            self.shape.setx(x + round(self.dx, 5))

    # Method to check if a player has lost (ball has crossed left or right boundary)
    def check_player_loss(self):
        # Get the current x coordinate of the ball
        x = round(self.shape.xcor(), 5)

        # If the ball goes beyond the left or right side of the screen (x > 390 or x < -390)
        if 0 < x > 390 or 0 > x < -390:
            # Toggle the flag to switch sides (1 means right side, 0 means left side)
            self.flag = 1 - self.flag  

            # If the ball went off the left side (flag == 1), Player 2 scores a point
            if not (self.flag == 1):
                self.score.score_player2 += 1   # Increase Player 2's score
                self.score.score.clear()        # Clear the current score display
                self.score.view_score()         # Update the score display
                self.shape.goto(0, 0)           # Reset ball position to center
                self.dy = 0.15                   # Reset vertical speed
                self.dx = 0.15                   # Reset horizontal speed

            # If the ball went off the right side (flag == 0), Player 1 scores a point
            else:
                self.score.score_player1 += 1   # Increase Player 1's score
                self.score.score.clear()        # Clear the current score display
                self.score.view_score()         # Update the score display
                self.shape.goto(0, 0)           # Reset ball position to center
                self.dy = -0.15                  # Reverse the vertical speed
                self.dx = -0.15                  # Reverse the horizontal speed

    # Method to detect collisions between the ball and the paddles (madrabs)
    def detect_madrab_hit(self, madrab2_x, madrab2_y, madrab1_x, madrab1_y):
        # Check if the ball hits the right paddle (Madrab 2)
        if (
            340 < self.shape.xcor()  < 350
        ) and (
            madrab2_y - 50 < self.shape.ycor() < madrab2_y + 50
        ):
            # Toggle flag to indicate the ball is moving to the left
            self.flag = 1 - self.flag  
            # Reverse the horizontal direction of the ball
            self.dx *= -1
            self.shape.setx(340)

        # Check if the ball hits the left paddle (Madrab 1)
        if (
            -340 > self.shape.xcor() > -350
        ) and (
            madrab1_y - 50 < self.shape.ycor() < madrab1_y + 50
        ):
            # Toggle flag to indicate the ball is moving to the right
            self.flag = 1 - self.flag
            # Reverse the horizontal direction of the ball
            self.dx *= -1
            self.shape.setx(-340)

