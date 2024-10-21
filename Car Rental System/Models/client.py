from sys import path 
from os.path import  dirname 
from os import getcwd

path.insert(0 , dirname(getcwd()))



from Controler.opertion_manager import clientOpertionManager
from .user import User
from Controler.auth import Login
from Controler.Input_Handler import InputHandler 


class Client (User):  


    def showList(self):

        output_message = """
Welcome Client 

1 - View All Cars 
2- View Car By Id 
3 - Rent Car 
4 - Return Car 
5 - Show my Rents  
6 - Edit My Data  
7 - Change Password
8 - Quit  
Enter Your Choice (1-7) : """
        
        choice =  InputHandler.Enter_Valid_choice(outputMessage=output_message , choices_numbers=8)


        if 3<= choice <=7:
            clientOpertionManager.excute_opertion(idx=choice , user_id=self.ID ) 
            
        elif choice == 8 : 
            quit()
        
        else : 
            clientOpertionManager.excute_opertion(idx=choice) 
        # Client.showList()


    def __str__(self):
        return "Client User Information : \n" + super().__str__()     
 