       #  if (
       #      madrab2.shape.xcor() - 20 < ball.shape.xcor() < madrab2.shape.xcor() + 20
       #  ) and (
       #      madrab2.shape.ycor() - 50 < ball.shape.ycor() < madrab2.shape.ycor() + 50
       #  ):
       #      ball.flag = 1 - ball.flag  # 1 > right   0 > left
       #      ball.dx *= -1

       #  if (
       #      madrab1.shape.xcor() - 20 < ball.shape.xcor() < madrab1.shape.xcor() + 20
       #  ) and (
       #      madrab1.shape.ycor() - 50 < ball.shape.ycor() < madrab1.shape.ycor() + 50
       #  ):
       #      ball.flag = 1 - ball.flag  # 1 > right   0 > left
       #      ball.dx *= -1







# import turtle
# from Madrab import Madrab
# from Ball import Ball


# import turtle

# # Initialize player movement flags
# player1_up = False
# player1_down = False
# player2_up = False
# player2_down = False

# # Function to move player 1 up
# def player1_up_press():
#     global player1_up
#     player1_up = True

# # Function to move player 1 down
# def player1_down_press():
#     global player1_down
#     player1_down = True

# # Function to move player 2 up
# def player2_up_press():
#     global player2_up
#     player2_up = True

# # Function to move player 2 down
# def player2_down_press():
#     global player2_down
#     player2_down = True

# # Functions to reset flags when keys are released
# def player1_up_release():
#     global player1_up
#     player1_up = False

# def player1_down_release():
#     global player1_down
#     player1_down = False

# def player2_up_release():
#     global player2_up
#     player2_up = False

# def player2_down_release():
#     global player2_down
#     player2_down = False

# # Function to check input and move the paddles accordingly
# def move_paddles(madrab1, madrab2):
#     if player1_up:
#         madrab1.shape_move_up()
#     if player1_down:
#         madrab1.shape_move_down()
#     if player2_up:
#         madrab2.shape_move_up()
#     if player2_down:
#         madrab2.shape_move_down()

#     # Repeat this function periodically
#     turtle.ontimer(lambda: move_paddles(madrab1, madrab2), 20)

# # Main game setup
# if __name__ == "__main__":
#     # Initialize the game window
#     wind = turtle.Screen()

#     # Set background color to black
#     wind.bgcolor("black")

#     wind.listen()

#     # Bind keypress and key release events
#     wind.onkeypress(player1_up_press, "w")
#     wind.onkeypress(player1_down_press, "s")
#     wind.onkeyrelease(player1_up_release, "w")
#     wind.onkeyrelease(player1_down_release, "s")

#     wind.onkeypress(player2_up_press, "Up")
#     wind.onkeypress(player2_down_press, "Down")
#     wind.onkeyrelease(player2_up_release, "Up")
#     wind.onkeyrelease(player2_down_release, "Down")

#     # Initialize madrabs (paddles)
#     madrab1 = Madrab()  # Left paddle
#     madrab2 = Madrab()  # Right paddle
#     ball = Ball()

#     # Set initial properties of madrabs
#     madrab1.properties_of_shape(0, "square", "blue", (-350, 0), 5, 1)
#     madrab2.properties_of_shape(0, "square", "red", (350, 0), 5, 1)

#     # Start moving paddles by polling key states
#     move_paddles(madrab1, madrab2)

#     while True:
#         wind.update()



    # wind.onkeypress(lambda: key_down("w"), "w")
    # wind.onkeypress(lambda: key_down("s"), "s")
    # wind.onkeypress(lambda: key_down("Up"), "Up")
    # wind.onkeypress(lambda: key_down("Down"), "Down")


    # wind.onkeyrelease(lambda: key_up("w"), "w")
    # wind.onkeyrelease(lambda: key_up("s"), "s")
    # wind.onkeyrelease(lambda: key_up("Up"), "Up")
    # wind.onkeyrelease(lambda: key_up("Down"), "Down")



# # Dictionary to hold the state of the keys
# keys_pressed = {
#     "w": False,
#     "s": False,
#     "Up": False,
#     "Down": False,
# }




# # Function to handle key press events
# def key_down(key) :
#     keys_pressed[key] = True

# # Function to handle key release events
# def key_up(key):
#     keys_pressed[key] = False



        # # Move paddles based on key states
        # if keys_pressed["w"]:
        #     madrab1.shape_move_up()
        # if keys_pressed["s"]:
        #     madrab1.shape_move_down()
        # if keys_pressed["Up"]:
        #     madrab2.shape_move_up()
        # if keys_pressed["Down"]:
        #     madrab2.shape_move_down()