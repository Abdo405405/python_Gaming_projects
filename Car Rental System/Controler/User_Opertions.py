import sys
from os.path import dirname, join
from os import getcwd
from termcolor import colored 
from tabulate import tabulate

# Add the parent directory of 'Models' to the system path
sys.path.insert(0, join(dirname(getcwd()), ""))


from Models.database import Database, Error
from Input_Handler import InputHandler


class AddNewAdmin:
    firstName = None
    lastName = None
    email =None
    phoneNumber = None
    password =None
    user_type = 1


    @classmethod 
    def operation (cls) : 
        cls.new_data()
        if cls.check_if_email_is_already_exist(cls.email) : 
            print (colored("This Account is already Exist " , 'yellow'))
            print('Please Register Again\n')
            cls.operation()
        else : 
            cls.save_data()
            print(colored("A New Admin has been successfully added." ,'green'))
            input(colored("\n\nEnter To Return To Main Menu" , 'yellow'))



    @classmethod
    def new_data (cls) :
        cls.firstName =InputHandler.Enter_Valid_Name(outputMessage="Enter First Name :  ")
        cls.lastName = InputHandler.Enter_Valid_Name(outputMessage="Enter Last Name :  ")
        cls.email = InputHandler.Enter_Valid_Email(outputMessage="Enter Email :  ")
        cls.phoneNumber =InputHandler.Enter_Valid_Phone(outputMessage="Enter Phone Number  :  ")
        cls.password = input("Enter password  :  ")



    @classmethod
    def check_if_email_is_already_exist (cls,email) :
        mycursor = Database.enable_conection () 
        mycursor.execute('select `email` from users ')
        results =[ row[0] for row in mycursor.fetchall()]

        if email in results : 
            return True 
        
        return False
    


    @classmethod
    def save_data(cls):

        mycursor = Database.enable_conection()


        insert_query = """
            INSERT INTO `users` 
            ( `FirstName` , `LastName`, `Email`, `PhoneNumber`, `Password`, `Type`) 
            VALUES ( %s, %s, %s, %s, %s, %s)
            """

        try:
            mycursor.execute(
                insert_query,
                (cls.firstName, cls.lastName, cls.email, cls.phoneNumber, cls.password, cls.user_type),
            )
            Database.connection.commit()
            Database.close_connection()

        except Error as e:
            raise RuntimeError("Sql Syntax Erorr ")




class AddNewClient:
    firstName = None
    lastName = None
    email =None
    phoneNumber = None
    password =None
    user_type = 0


    @classmethod 
    def operation (cls) : 
        cls.new_data()
        if cls.check_if_email_is_already_exist(cls.email) : 

            print (colored("This Account is already Exist " , 'yellow'))
            print('Please Register Again\n')
            cls.operation()

        else : 
            cls.save_data()
            print(colored("Your Account has been successfully created" ,'green'))
            input(colored("\n\nEnter To Return To Main Menu" , 'yellow'))



    @classmethod
    def new_data (cls) :
        cls.firstName =InputHandler.Enter_Valid_Name(outputMessage="Enter First Name :  ")
        cls.lastName = InputHandler.Enter_Valid_Name(outputMessage="Enter Last Name :  ")
        cls.email = InputHandler.Enter_Valid_Email(outputMessage="Enter Email :  ")
        cls.phoneNumber =InputHandler.Enter_Valid_Phone(outputMessage="Enter Phone Number  :  ")
        cls.password = input("Enter password  :  ")



    @classmethod
    def check_if_email_is_already_exist (cls,email) :
        mycursor = Database.enable_conection () 
        mycursor.execute('select `email` from users ')
        results =[ row[0] for row in mycursor.fetchall()]

        if email in results : 
            return True 
        
        return False
    


    @classmethod
    def save_data(cls):

        mycursor = Database.enable_conection()


        insert_query = """
            INSERT INTO `users` 
            ( `FirstName` , `LastName`, `Email`, `PhoneNumber`, `Password`, `Type`) 
            VALUES ( %s, %s, %s, %s, %s, %s)
            """

        try:
            mycursor.execute(
                insert_query,
                ( cls.firstName, cls.lastName, cls.email, cls.phoneNumber, cls.password, cls.user_type),
            )
            Database.connection.commit()
            Database.close_connection()

        except Error as e:
            raise RuntimeError("Sql Syntax Erorr ")
        



class EditProfileById : 

    @classmethod 

    def operation (cls , user_id) : 

        try : 
            cls.mycursor = Database.enable_conection() 

            # View data Before Update it 
            cls.view_data(id=user_id)

            field , value = cls.choice_field_to_update()
            
            query = f" update users set `{field}` = %s where `ID` = %s ;"

            cls.mycursor.execute(query , (value , user_id ) ) 
            Database.connection.commit()

            # View data After Update it 
            cls.view_data(user_id , field)

            Database.close_connection()
            
        except Error as err : 
            raise RuntimeError (err)
        


    @staticmethod
    def choice_field_to_update () :
            Output_message = """
1 - FirstName
2 - LastName
3 - Email
4 - PhoneNumber
5 - Password

Choice The Filed that you want To Update It : """
            field_mapping = {
                1: "FirstName",
                2: "LastNamr",
                3: "Email",
                4: "PhoneNumber",
                5: "Password",
            }

            choice = InputHandler.Enter_Valid_choice(outputMessage=Output_message , choices_numbers=5)
            field = field_mapping[choice]

            value = input ("Enter A new Value : ")

            return field , value


    @classmethod
    def view_data (cls , id=None ,field=None )  :

        query = """
SELECT 
    `ID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `Password`,
    CASE 
        WHEN `Type` = 1 THEN 'Admin'
        WHEN `Type` = 0 THEN 'Client'
    END AS "Type"
FROM 
    users  where `ID` = %s;
"""
        cls.mycursor.execute(query , (id , ) ) 
        sql_query = cls.mycursor.fetchall()

        if sql_query :
            headers=["ID" , "FirsrtName" , "LastName" , "Email" , "PhoneNumber" , "Password" , "Type"]
            headers = [colored(text , color='light_cyan') for text in headers]
            print(tabulate( headers=headers, tabular_data=sql_query , tablefmt='heavy_grid'))

        else : 
            print (colored("No Data To Show " , color='yellow'))


        
        if field :
            print(colored(f"Field {field} has been Updated  Successfully " , 'green'))
            input("\n\nEnter To return Main Menu ")






class ChangePassword : 

    @classmethod 

    def operation (cls , user_id) : 

        try : 
            cls.mycursor = Database.enable_conection() 


            # Enture From Old Password Before make Changing 
            while True :
                 old_password = input("Enter Old Password : ") 
                 query = f" SELECT Password FROM users  where `ID` = %s ;"
                 cls.mycursor.execute(query , (user_id , ) ) 
                 current_password = cls.mycursor.fetchone()[0]
                 if current_password == old_password : 
                     break
                 else : 
                     print(colored("\nWrong Password\n" , 'red'))


            new_password  = input("Enter New Password : ") 
            confirem_password = input("Confirm Password : ")
            while True : 
                if new_password == confirem_password : 
                    break 

                else : 
                    print(colored("\nDoesn't Match \n" , 'red'))
                    new_password  = input("Enter New Password agin : ") 
                    confirem_password = input("Confirm Password : ")


            query = f" update users set `Password` = %s where `ID` = %s ;"

            

            cls.mycursor.execute(query , (new_password , user_id ) ) 
            Database.connection.commit()
            print(colored("\nYour password has been successfully changed. \n" , 'green'))
            input(colored("Enter To Return Main Menu " , 'yellow'))




            Database.close_connection()
            
        except Error as err : 
            raise RuntimeError (err)
        









 
