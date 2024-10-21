
from abc import ABCMeta , abstractmethod

class User (metaclass = ABCMeta): 
    def __init__(self):
        self.__ID = None 
        self.__firstName = None 
        self.__lastName = None 
        self.__email = None 
        self.__phonenumber = None 
        self.__password = None
        self.__user_type = None


    @property 
    def ID (self ) : 
        return self.__ID 

    @ID.setter
    def ID (self , value ) :
        self.__ID = value 

    @property 
    def user_type (self ) : 
        return self.__user_type

    @user_type.setter
    def user_type (self , value ) :
        self.__user_type = value 

    @property 
    def firstName (self ) : 
        return self.__firstName 

    @firstName.setter
    def firstName (self , value ) :
        self.__firstName = value 

    @property 
    def lastName (self ) : 
        return self.__lastName 

    @lastName.setter
    def lastName (self , value ) :
        self.__lastName = value 


    @property 
    def email (self ) : 
        return self.__email 

    @email.setter
    def email (self , value ) :
        self.__email = value 

    @property 
    def phonenumber (self ) : 
        return self.__phonenumber 

    @phonenumber.setter
    def phonenumber (self , value ) :
        self.__phonenumber = value 

    @property 
    def password (self ) : 
        return self.__password 

    @password.setter
    def password (self , value ) :
        self.__password = value 


    @abstractmethod 
    def showList () : 
        pass


    def __str__(self):
         return (
              f"FirstName : {self.firstName}\n"
              f"LastName : {self.firstName}\n"
              f"Email : {self.email}\n"
              f"PhoneNumber : {self.phonenumber}\n"

         )








        