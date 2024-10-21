from os import system

from User_Opertions import AddNewAdmin  ,EditProfileById , ChangePassword
from Car_Opertions import ViewCarById , ViewCars , AddCar  ,UpdateCarById ,DeleteCarBYId 
from Rent_Opertions import RentCar , ReturnCar ,ShowUserRents ,ShowAllRents 

from abc import ABCMeta , abstractmethod
def clean_screen():
    system("cls")



class OpertionManager(metaclass = ABCMeta):


    @abstractmethod
    def excute_opertion(idx):
        pass

        



class AdminOpertionManager (OpertionManager) : 
    opertions = (
        AddNewAdmin.operation,
        AddCar.operation,
        ViewCars.operation , 
        ViewCarById.operation , 
        UpdateCarById.operation , 
        DeleteCarBYId.operation , 
        ShowAllRents.operation , 


    )

    def excute_opertion(idx):

        if 0 <= idx <= len(AdminOpertionManager.opertions):
            AdminOpertionManager.opertions[idx - 1]()

        else:
            raise KeyError("Invalid Opertion Index ")





class clientOpertionManager (OpertionManager) : 
    opertions = (
        ViewCars.operation , 
        ViewCarById.operation , 
        RentCar.operation , 
        ReturnCar.operation , 
        ShowUserRents.operation ,
        EditProfileById.operation , 
        ChangePassword.operation

    )

    def excute_opertion(idx , user_id =None):

        if 0 <= idx <= len(clientOpertionManager.opertions) and user_id == None :
            clientOpertionManager.opertions[idx - 1]()

        elif  0 <= idx <= len(clientOpertionManager.opertions) and user_id:
            clientOpertionManager.opertions[idx - 1](user_id = user_id)

        else:
            raise KeyError("Invalid Opertion Index ")

        



