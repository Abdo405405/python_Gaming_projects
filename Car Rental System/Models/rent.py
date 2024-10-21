
from datetime import datetime

class Rent  : 

    def __init__(self):
            self.__ID = None
            self.__user_id = None 
            self.__car_id = None 
            self.__car_reservation_time = None 
            self.__status = None 
            self.__hours = None
            self.__total = None

    
    @property 
    def ID (self ) : 
        return self.__ID 

    @ID.setter
    def ID (self , value ) :
        self.__ID = value 


    @property 
    def user_id (self ) : 
        return self.__user_id 

    @user_id.setter
    def user_id (self , value ) :
        self.__user_id = value 

    @property 
    def car_id (self ) : 
        return self.__car_id 

    @car_id.setter
    def car_id (self , value ) :
        self.__car_id = value 


    @property 
    def car_reservation_time (self ) : 
        return self.__car_reservation_time 

    @car_reservation_time.setter
    def car_reservation_time (self , value ) :
        self.__car_reservation_time = datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")

    @property 
    def status (self ) : 
        return self.__status 

    @status.setter
    def status (self , value ) :
        self.__status = value 

    @property 
    def hours (self ) : 
        return self.__hours 

    @hours.setter
    def hours (self , value ) :
        self.__hours = value 


    @property 
    def total (self ) : 
        return self.__total 

    @total.setter
    def total (self , value ) :
        self.__total = value 


    @property 
    def status (self ) : 
        return self.__status 

    @status.setter
    def status (self , value ) :
        self.__status = value 


    def __str__(self):
         return (
              f"ID : {self.ID}\n"
              f"user_id : {self.user_id}\n"
              f"car_id : {self.car_id}\n"
              f"car_reservation_time : {self.car_reservation_time}\n"
              f"status : {self.status}\n"
              f"hours : {self.hours}\n"
              f"total : {self.total}\n"

         )
        









        
