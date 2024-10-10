from turtle import Turtle

class Score:
    def __init__(self):
        # Create a Turtle object for displaying the score
        self.score = Turtle()

        # Set the text color to white
        self.score.color("white")

        # Hide the turtle shape so only text is displayed (no visible turtle icon)
        self.score.hideturtle()

        # Lift the pen up to prevent drawing lines when moving the turtle
        self.score.penup()

        # Set the turtle's speed to the fastest (0 means instant)
        self.score.speed(0)

        # Move the turtle to the top center of the screen to display the score
        self.score.goto(x=0, y=260)

        # Initialize player 1's score to 0
        self.score_player1 = 0

        # Initialize player 2's score to 0
        self.score_player2 = 0

        # Display the initial score on the screen
        self.view_score()

    def view_score(self):
        # Display the score of both players at the top of the screen
        # The format is "Player1: [score]   Player2: [score]"
        # 'align="center"' centers the text, and 'font' sets the font type, size, and style
        self.score.write(
            f"Player1 : {self.score_player1}                  Player2 : {self.score_player2}",
            align="center",
            font=("Courier", 24, "normal")
        )
