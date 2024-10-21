
from .user import User

from sys import path
from os.path import dirname, join
from os import getcwd


path.insert(0, join(dirname(getcwd()), ''))

from Controler.opertion_manager import AdminOpertionManager 
from Controler.Input_Handler import InputHandler


class Admin (User)  : 



    @staticmethod
    def showList():


        output_message = """
Welcome Admin 

1 - Add New Admin 
2 - Add New Car 
3- View Cars 
4- View Cars By Id  
5 - Update Car 
6- Delete Car 
7 - Show Rents 
8- Quit 
Enter Your choice (1-8) : """

        
      
        choice =  InputHandler.Enter_Valid_choice(outputMessage=output_message , choices_numbers=8)
   

        if choice == 8 : 
            quit()
             
        AdminOpertionManager.excute_opertion(idx=choice)
        # Admin.showList()

    def __str__(self):
        return "Admin User Information : \n" + super().__str__() 



if __name__ == "__main__" :
        ad = Admin()
        ad.showList()