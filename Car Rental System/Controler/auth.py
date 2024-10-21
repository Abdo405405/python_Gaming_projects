
from sys import path
from os import getcwd
from os.path import dirname
from termcolor import colored
from User_Opertions import AddNewClient
path.insert(0, dirname(getcwd()))

from Models.database import Database, Error
from Models import admin, client

        
class Login:
    """
    This Class To make User Looged in 
    it Return That User 

    """

    @classmethod
    def login(cls):
        try:
            mycursor = Database.enable_conection()

            while True:
                email = input("Enter Your Email (or -1 to create new one) : ")
                if email == '-1' : 
                    AddNewClient.operation()
                    mycursor = Database.enable_conection()
                    continue
                password = input("Enter Your Password: ")
                mycursor.execute(
                    "select * from users  where email = %s and password = %s ",
                    (email, password),
                )
                sql_query = mycursor.fetchone()

                if cls.check_if_userDate_is_correct(sql_query=sql_query) :
                    break


            cls.if_admin_or_client(sql_query=sql_query)

            cls.entring_data(user=cls.user, sql_query=sql_query)

            Database.close_connection()


            return cls.user
        

        except Error as err:
            print(err)

    @classmethod
    def entring_data(cls,user, sql_query):
        user.ID = sql_query[0]
        user.firstName = sql_query[1]
        user.lastName = sql_query[2]
        user.email = sql_query[3]
        user.phonenumber = sql_query[4]
        user.password = sql_query[5]
        user.user_type = sql_query[6]
            




    @classmethod
    def if_admin_or_client(cls,sql_query) : 
        cls.user= (
                admin.Admin() if sql_query[-1] == 1 else client.Client()
            )  # 1 > Admin 0 > client
        
    @classmethod
    def check_if_userDate_is_correct (cls ,sql_query) : 
            if sql_query:
                return True 
            else:
                print(colored("Wrong userName Or Password " , color='red'))
                return False
            



