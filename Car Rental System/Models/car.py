
class Car : 
    def __init__(self):
        self.__ID = None 
        self.__brand = None 
        self.__color = None 
        self.__year = None 
        self.__price = None
        self.__available = None

    @property 
    def ID (self ) : 
        return self.__ID 

    @ID.setter
    def ID (self , value ) :
        self.__ID = value 

    @property 
    def brand (self ) : 
        return self.__brand 

    @brand.setter
    def brand (self , value ) :
        self.__brand = value 


    @property 
    def color (self ) : 
        return self.__color 

    @color.setter
    def color (self , value ) :
        self.__color = value 

    @property 
    def year (self ) : 
        return self.__year 

    @year.setter
    def year (self , value ) :
        self.__year = value 

    @property 
    def price (self ) : 
        return self.__price 

    @price.setter
    def price (self , value ) :
        self.__price = value 


    @property 
    def available (self ) : 
        return self.__available 

    @available.setter
    def available (self , value ) :
        self.__available = value 








        