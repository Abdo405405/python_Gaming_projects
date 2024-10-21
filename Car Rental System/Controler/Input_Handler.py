

from termcolor import colored

from re import compile 

from datetime import datetime


class InputHandler : 

    @staticmethod 
    def Enter_Valid_choice (outputMessage,choices_numbers) :

        while True :

            inp = input(outputMessage)

    
            try : 
                if not inp.isnumeric() : 
                    raise ValueError ("\nOnly Numbrs is Allowed\n") 
                
    
                if 0 >= int(inp) or  choices_numbers < int(inp): 
                    raise ValueError ("\nPlease Enter Valid Choice\n") 
    
            except ValueError as verr :
                print(colored(verr , 'red'))
            
    
            else  : 
                return int (inp)
            


    @staticmethod 
    def Enter_Valid_Name (outputMessage) : 

        pattern = compile(r'^[A-Za-z]+$')
        err_pattern = compile(r'[\W\d_]+')


        while True :

            inp = input(outputMessage).strip()

    
            try : 
                if not pattern.match(inp) :
                    r = err_pattern.search(inp).group(0)
                    if r.isdigit() :
                        m = "numbers is not allowed "

                    else:
                         m = "special character is not allowed "



                    raise ValueError (f"\nInvalid Name ({m}) \n") 
                
    
            except ValueError as verr :
                print(colored(verr , 'red'))
            
    
            else  : 
                return inp
            


    @staticmethod 
    def Enter_Valid_Email (outputMessage) : 

        pattern = compile(r'^[A-z0-9]+@(gmail|yahoo|hotmail)\.(com)$')


        while True :

            inp = input(outputMessage).strip()

    
            try : 
                if not pattern.match(inp) :

                    raise ValueError (f"\nInvalid Email  \n") 
                
    
            except ValueError as verr :
                print(colored(verr , 'red'))
            
    
            else  : 
                return inp
            

    @staticmethod 
    def Enter_Valid_Phone (outputMessage) : 

        pattern = compile(r'^(011|012|015|010)[\d]{8}$')


        while True :

            inp = input(outputMessage).strip()

    
            try : 
                if not pattern.match(inp) :

                    raise ValueError (f"\nInvalid PhoneNumber  \n") 
                
    
            except ValueError as verr :
                print(colored(verr , 'red'))
            
    
            else  : 
                return inp
            
    
    def Enter_Valid_Year (outputMessage) :

        while True :

            inp = input(outputMessage).strip()
    
            try : 
                    
                    if not inp.isnumeric() : 
                        raise ValueError (f"\nInvalid Year : Year Must Integers like this YYYY   \n") 
                                    
                                    
                    inp = datetime(year=int(inp) , month=1 , day=1)

                    
                    if inp > datetime.now():
                        raise ValueError (f"\nInvalid year: The year cannot be in the future. \n") 
                
    
            except ValueError as verr :
                print(colored(verr , 'red'))
            
    
            else  : 
                return inp




