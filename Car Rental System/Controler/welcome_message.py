from termcolor import colored 



def Welcome_Message () : 
    Welcome_Message = colored(" Welcome To Car Rental Management System " , color='green') 

    print(Welcome_Message.center(len(Welcome_Message) + 75 , '#'))