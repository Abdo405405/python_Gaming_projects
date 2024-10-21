from os.path import dirname, join
from sys import path
from os import getcwd
from termcolor import colored
from datetime import datetime
from tabulate import tabulate
path.insert(0, join(dirname(getcwd()), ""))

from Models.database import Database, Error
from Models.rent import Rent


class RentCar:

    @classmethod
    def operation(cls, user_id):

        cls.mycursor = Database.enable_conection()
        while True:

            try:
                id = input("Eneter Id of Car ( -1 to cancel) : ")
                if id == "-1":
                    break

                if cls.check_if_id_is_valid(car_id=id) == False:
                    raise ValueError(colored("\nInvalid Id\n", "red"))

                if cls.Car_status(car_id=id):

                    raise ValueError(f"\n{cls.Car_status(car_id= id)}\n")

                cls.fill_data(user_id=user_id, car_id=id)
                cls.update_car_table(car_id=id)
                cls.save_data()

            except ValueError as v_err:
                print(v_err)

            else:
                print(colored("\nCar rental successfully recorded!\n", "green"))
                Database.close_connection()
                input(colored("\nEnter To Retun Main Menu\n"))
                break

    @classmethod
    def check_if_id_is_valid(cls, car_id):
        """
        - check if car is already exist in cars table
        return false if it does not exist
        return true if it exists
        """
        try:
            cls.mycursor.execute("SELECT `ID` FROM cars WHERE `ID` = %s ", (car_id,))

        except Error as err:
            raise RuntimeError(err)

        else:
            return True if cls.mycursor.fetchone() else False

    @classmethod
    def fill_data(cls, user_id, car_id):

        cls.mycursor.execute("SELECT `Price` FROM  cars WHERE `ID` = %s ", (car_id,))
        price_per_hour = cls.mycursor.fetchone()[0]
        cls.user_id = user_id
        cls.car_id = car_id
        cls.hours = int(
            input("Enter the number of hours you want to rent the car for : ")
        )
        cls.Date_Time = datetime.now()
        cls.status = 1
        cls.total_price = cls.hours * price_per_hour

    @classmethod
    def save_data(cls):
        query = """
        INSERT INTO `rents` (`user_id` , `car_id` , `DateTime` , `Hours` , `Total` , `Status` ) 
        VALUES ( %s  , %s  ,%s  ,%s  ,%s  ,%s )
         """
        cls.mycursor.execute(
            query,
            (
                cls.user_id,
                cls.car_id,
                cls.Date_Time,
                cls.hours,
                cls.total_price,
                cls.status,
            ),
        )
        Database.connection.commit()

    @classmethod
    def update_car_table(cls, car_id):
        try:
            query = """ 
            UPDATE cars set `Available` = 2  WHERE ID = %s
             """
            cls.mycursor.execute(query, (car_id,))
            Database.connection.commit()

        except Error as err:
            raise RuntimeError("Error in Update  car Table while Renting  Process   ")

    @classmethod
    def Car_status(cls, car_id):
        cls.mycursor.execute(
            "SELECT `Available` FROM  cars WHERE `ID` = %s ", (car_id,)
        )
        result = cls.mycursor.fetchone()[0]
        if result == 0:
            return colored("Car Is UnAvailable ", "red")
        elif result == 2:
            return colored("Car Is Already Rented ", "yellow")

        else:
            return None


class ReturnCar:

    @classmethod
    def user_rent_data(cls, user_id):
        try:
            cls.mycursor.execute(
                "SELECT * FROM rents WHERE `user_id` = %s ", (user_id,)
            )

        except Error as err:
            raise RuntimeError("Error in checking id  ")

        else:
            user_rent_data = cls.mycursor.fetchall()
            if user_rent_data:
                list_of_rents = []
                for row in user_rent_data:
                    rend_object = Rent()
                    rend_object.ID = row[0]
                    rend_object.user_id = row[1]
                    rend_object.car_id = row[2]
                    rend_object.car_reservation_time = row[3]
                    rend_object.hours = row[4]
                    rend_object.total = row[5]
                    rend_object.status = row[6]
                    list_of_rents.append(rend_object)

                cls.user_rents = list_of_rents
                return True

            else:
                print(colored("\nUser Does't has any Rents\n", "red"))
                return False

    @classmethod
    def operation(cls, user_id):

        cls.mycursor = Database.enable_conection()

        if cls.user_rent_data(user_id=user_id):

            while True:

                try:
                    id = input("Eneter Id of Car ( -1 to cancel) : ")
                    if id == "-1":
                        break

                    if cls.check_if_id_is_valid(car_id=id)[0] == False:
                        raise ValueError(cls.check_if_id_is_valid(car_id=id)[1])

                    cls.delete_data(user_id=user_id, car_id=id)
                    cls.update_car_table(car_id=id)

                except ValueError as v_err:
                    print(v_err)

                else:
                    print(colored("\nCar  successfully  Return !\n", "green"))
                    Database.close_connection()
                    break

        input(colored("\nEnter To Retun Main Menu\n" , 'yellow'))

    @classmethod
    def check_if_id_is_valid(cls, car_id):

        for user_rent in cls.user_rents:
            if user_rent.car_id == int(car_id):
                return True, True

        return False, colored("\nUser Does't Rent This Car To Return\n", "yellow")

    @classmethod
    def delete_data(cls, user_id, car_id):
        try:
            query = """
           DELETE FROM `rents`  WHERE user_id = %s and car_id = %s 
            """
            cls.mycursor.execute(query, (user_id, car_id))
            Database.connection.commit()

        except Error as err:
            raise RuntimeError("Error in Delete rent ")

    @classmethod
    def update_car_table(cls, car_id):
        try:
            query = """ 
           UPDATE cars set `Available` = 1 WHERE ID = %s
            """
            cls.mycursor.execute(query, (car_id,))
            Database.connection.commit()

        except Error as err:
            raise RuntimeError("Error in Update  car Table while returning Process   ")


class ShowUserRents:
    
    @classmethod
    def user_rent_data(cls, user_id):
        try:
            cls.mycursor.execute(
                "SELECT * from `cars` WHERE ID IN (SELECT `car_id` FROM `rents` WHERE user_id = %s)", (user_id,)
            )

            cls.user_rents = cls.mycursor.fetchall()
        except Error as err:
            raise RuntimeError("Error in checking id  ")
            

    @classmethod
    def operation(cls, user_id):
        cls.mycursor = Database.enable_conection()
        cls.user_rent_data(user_id=user_id)
        if cls.user_rents : 
            headers=["ID" , "Brand" , "Model" , "Color" , "Year" , "Price" , "Status"]
            headers = [colored(text , color='light_cyan') for text in headers]
            print(tabulate( headers=headers, tabular_data=cls.user_rents , tablefmt='heavy_grid'))


        else : 
            print(colored("\nNo Data To Show\n" , 'yellow'))
            
         
        input(colored("\nEnter To Retun Main Menu\n" , 'yellow'))




class ShowAllRents:
    
    @classmethod
    def show_all_rent_data(cls):
        try:
            cls.mycursor.execute(
                """
               SELECT 
               rents.ID,
               users.FirstName AS user_name,           -- Replace `user_id` with user name (or other details from users table)
               cars.Model AS car_model,           -- Replace `car_id` with car model (or other details from cars table)
               rents.DateTime,
               rents.Hours,
               rents.Total,
               CASE 
               WHEN `Status` = 1 THEN 'Running'
               WHEN `Status` = 0 THEN 'Returned'
               END AS "Status"
               FROM 
                   rents
               JOIN 
                   users ON rents.user_id = users.ID  -- Join rents table with users table based on user_id
               JOIN 
                   cars ON rents.car_id = cars.ID     -- Join rents table with cars table based on car_id
               ORDER BY 
                   rents.ID;                                 
                """ )

            cls.user_rents = cls.mycursor.fetchall()
        except Error as err:
            raise RuntimeError("Error in Sql Syntax  ")
            

    @classmethod
    def operation(cls):
        cls.mycursor = Database.enable_conection()
        cls.show_all_rent_data()
        if cls.user_rents : 
            headers=["ID" , "UserName" , "Model" , "Data Time" , "Hours" , "Price" , "Status"]
            headers = [colored(text , color='light_cyan') for text in headers]
            print(tabulate( headers=headers, tabular_data=cls.user_rents , tablefmt='heavy_grid'))


        else : 
            print(colored("\nNo Data To Show\n" , 'yellow'))
            
        input(colored("\nEnter To Retun Main Menu\n" , 'yellow'))



