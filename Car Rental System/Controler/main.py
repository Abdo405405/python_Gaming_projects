from auth import Login 
from welcome_message import Welcome_Message
from time import sleep
from os import system

def clean_screen():
    system('cls')


def Car_Rental_System () : 
    Welcome_Message()

    user = Login.login()

    while True :
       clean_screen()
       Welcome_Message()
       user.showList()






Car_Rental_System()
