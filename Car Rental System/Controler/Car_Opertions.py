import sys
from os.path import dirname, join
from os import getcwd
from termcolor import colored
from tabulate import tabulate 


# Add the parent directory of 'Models' to the system path
sys.path.insert(0, join(dirname(getcwd()), ""))


from Models.database import Database, Error
from Input_Handler import InputHandler


class AddCar:
    Brand = None
    Model = None
    Color =None
    Year = None
    is_Available = 0



    @classmethod 
    def operation (cls) : 
        cls.new_data()
        cls.save_data()
        print(colored("Car Added successfully" , 'green')) 
        input("Enter To Return Main Menu ")





    @classmethod
    def new_data (cls) :
        cls.Brand = input("Enter Brand Name :  ")
        cls.Model = input("Enter Model Name :  ")
        cls.Color = input("Enter Car Color :  ")
        cls.Year = input("Enter Year  :  ")



    
    @classmethod
    def save_data(cls):

        mycursor = Database.enable_conection()

        # mycursor.execute("SELECT COUNT(*) FROM `cars` ")

        # id = mycursor.fetchone()[0]

        insert_query = """
            INSERT INTO `cars` 
            ( `Brand` , `Model`, `Color`, `Year` , `Available`) 
            VALUES (%s, %s, %s, %s, %s)
            """

        try:
            mycursor.execute(
                insert_query,
                (cls.Brand, cls.Model, cls.Color, cls.Year ,  cls.is_Available),
            )
            Database.connection.commit()
            Database.close_connection()

        except Error as e:
            raise RuntimeError("Sql Syntax Erorr ")



class ViewCars : 

    @staticmethod 
    def operation () : 
        mycursor=Database.enable_conection() 

        query = """
SELECT 
    `ID`, `Brand`, `Model`, `Color`, `Year`, `Price`,
    CASE 
        WHEN `Available` = 1 THEN 'Available'
        WHEN `Available` = 2 THEN 'Rented'
        ELSE 'Unavailable'
    END AS "Status"
FROM 
    cars;

"""
        mycursor.execute(query) 
        sql_query = mycursor.fetchall()

        if sql_query :
            headers=["ID" , "Brand" , "Model" , "Color" , "Year" , "Price" , "Status"]
            headers = [colored(text , color='light_cyan') for text in headers]
            print(tabulate( headers=headers, tabular_data=sql_query , tablefmt='heavy_grid'))

        else : 
            print (colored("No Data To Show " , color='yellow'))


        input("\nEnter To return Main Menu ")


class ViewCarById : 

    @staticmethod 
    def operation () : 
        mycursor=Database.enable_conection() 

        id = input("Enter The Car ID : ")

        query = """
SELECT 
    `ID`, `Brand`, `Model`, `Color`, `Year`, `Price`,
    CASE 
        WHEN `Available` = 1 THEN 'Available'
        WHEN `Available` = 2 THEN 'Rented'
        ELSE 'Unavailable'
    END AS "Status"
FROM 
    cars

WHERE `ID` = %s ;

"""
        mycursor.execute(query , (id , ) ) 
        sql_query = mycursor.fetchall()

        if sql_query :
            headers=["ID" , "Brand" , "Model" , "Color" , "Year" , "Price" , "Status"]
            headers = [colored(text , color='light_cyan') for text in headers]
            print(tabulate( headers=headers, tabular_data=sql_query , tablefmt='heavy_grid'))

        else : 
            print (colored("No Data To Show " , color='yellow'))


        Database.close_connection()

        input("\nEnter To return Main Menu ")



class UpdateCarById : 

    @classmethod 

    def operation (cls) : 

        try : 
            cls.mycursor = Database.enable_conection() 
            id = input("Enter The Car ID : ")

            # View data Before Update it 
            cls.view_data(id=id)

            field , value = cls.choice_field_to_update()
            
            query = f" update cars set `{field}` = %s where `ID` = %s ;"

            cls.mycursor.execute(query , (value , id ) ) 
            Database.connection.commit()

            # View data After Update it 
            cls.view_data(id , field)

            Database.close_connection()
            
        except Error as err : 
            raise RuntimeError (err)
        


    @staticmethod
    def choice_field_to_update () :
            Output_message = """
1 - Brand 
2 - Model
3 - Color
4 - Year
5 - Price
6 - Status

Choice The Filed that you want To Update It : """
            field_mapping = {
                1: "Brand",
                2: "Model",
                3: "Color",
                4: "Year",
                5: "Price",
                6: "Available"
            }

            choice = InputHandler.Enter_Valid_choice(outputMessage=Output_message , choices_numbers=6)
            field = field_mapping[choice]
            print("Here >>>>>> ",field)

            if field == "Year" : 
                value = InputHandler.Enter_Valid_Year("Enter A new Value : ")

            else :
                value = input ("Enter A new value : ")



            return field , value


    @classmethod
    def view_data (cls , id=None ,field=None )  :

        query = """
SELECT 
    `ID`, `Brand`, `Model`, `Color`, `Year`, `Price`,
    CASE 
        WHEN `Available` = 1 THEN 'Available'
        WHEN `Available` = 2 THEN 'Rented'
        ELSE 'Unavailable'
    END AS "Status"
FROM 
    cars  where `ID` = %s;
"""
        cls.mycursor.execute(query , (id , ) ) 
        sql_query = cls.mycursor.fetchall()

        if sql_query :
            headers=["ID" , "Brand" , "Model" , "Color" , "Year" , "Price" , "Status"]
            headers = [colored(text , color='light_cyan') for text in headers]
            print(tabulate( headers=headers, tabular_data=sql_query , tablefmt='heavy_grid'))

        else : 
            print (colored("No Data To Show " , color='yellow'))


        
        if field :
            print(colored(f"Field {field} has been  Updated  Successfully " , 'green'))
            input("\n\nEnter To return Main Menu ")        



class DeleteCarBYId :

    @classmethod
    def operation (cls) :


        while True :
            try : 
                cls.mycursor = Database.enable_conection() 
    
                id = input("Enter The Car ID : ")

                if  DeleteCarBYId.check_if_car_doesnt__exist(id) : 
                    raise ValueError (colored("\nPlease Enter Valid ID \n" , 'red'))
       
            except Error as err : 
                raise RuntimeError (err)
            
            except ValueError as err : 

                print(err)
            

            else : 
    
                query = " DELETE FROM cars WHERE `ID` = %s"
    
                cls.mycursor.execute(query , ( id ,  ) )
    
    
                Database.connection.commit()
    
                print(colored(f"Car With Id : {id} Deleted Successfully" , 'green'))
    
                input(colored("\n\nEnter To Return To Main Menu" , 'yellow'))
                Database.close_connection()
                break


            
    @classmethod
    def check_if_car_doesnt__exist(cls , id) : 
        query = " SELECT * from cars WHERE `ID` = %s"
        cls.mycursor.execute(query , ( id ,  ) )
        car = cls.mycursor.fetchone() 

        return True if car == None else False




