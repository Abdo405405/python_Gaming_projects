import mysql.connector 

from mysql.connector import Error

class Database : 

    @classmethod 
    def enable_conection (cls) :
            
        try : 
            connection =  mysql.connector.connect(
            host = "localhost" ,
            user ='root' , 
            password ="" ,
            database = 'carrentalsystem'
        )
            
            cls.connection = connection
            cls.mycursor = connection.cursor()
            return  connection.cursor()
        
        except mysql.connector.Error as err : 
             raise RuntimeError ("Error While Database Connection ")
    
    
    @classmethod
    def close_connection (cls) : 
          cls.mycursor.close()
          cls.connection.close()

    










