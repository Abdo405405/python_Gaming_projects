import tabulate
import os 
import time
import json
def clean_screen () : 
    os.system('cls')

    
class Task : 
    def __init__(self ,data) -> None:
        self.__tasks = data
        self.__status = False

    @property
    def tasks(self) : 
        return self.__tasks 
    
    def check_erorrs (self,printedMessage,flag=True) : 
        while True : 
         try : 
             self.show_tasks()
             taskName = input(f"{printedMessage}").strip()
             if not taskName.isalpha() : 
                 raise ValueError ("Invalid Input : Task Should Be only Letters ") 
             if taskName not in  self.__tasks and flag: 
                     raise KeyError (f"Task \"{taskName}\" does not Exist")
         except (ValueError,KeyError) as e :
             clean_screen()
             print (f"{e}")
         else :
            return taskName

    def Add_Task (self) : 
        printedMessage = "Enter Your Task Name : "
        taskName =self.check_erorrs(printedMessage ,flag=False)
        self.__tasks[f"{taskName.lower()}"]= {"is_complete":False , "note" : "" }
        clean_screen()
        print("Task Added Successfully")
             
    def Remove_Task (self) : 
        printedMessage = "Enter The Task You want To Delete It : "
        TaskName = self.check_erorrs(printedMessage)
        del self.tasks[TaskName.lower()]
        print("Task deleted Successfully")

    def mark_task_as_complete_or_incomplete (self) : 
        printedMessage = "Enter the task you want to change its status : "
        TaskName = self.check_erorrs(printedMessage)             
        self.tasks[TaskName.lower()]["is_complete"]  =  not self.__status
        self.__status = not self.__status
        print("Task Status changed Successfully")

    def Task_Note (self) : 
        printedMessage="Enter The Task you want to add note to it : "
        TaskName=self.check_erorrs(printedMessage)
        note=input("Enter A Note : ")
        print( "Note Added Successfully" if self.__tasks[TaskName]["note"]=="" else "Note updated Successfully"  )
        self.tasks[TaskName]["note"]  = note 
 
    def show_tasks (self) : 
        if self.tasks : 
            data =[]
            for task , details in self.tasks.items() : 
                data.append([task, details["note"],"✅" if details["is_complete"] else "❌" ])
            print(tabulate.tabulate(data ,headers=["Task" ,"Note" , "IS_Compelete"], tablefmt="heavy_grid"))
        else : 
            print(tabulate.tabulate([["No" , "Tasks" , "To Show" ]] ,headers=["Task" ,"Note" , "IS_Compelete"], tablefmt="heavy_grid"))

    def Quit (self) : 
        print("Have A Nice Day") 
        exit()   

class Menu : 
    @staticmethod
    def Task_menu () : 
        task_menu ="""
1 - Add Task 
2 - Change Status Of A Task
3 - Add Note To A Task
4 - Delete A Task 
5 - Quit

Your Choice: """
        choice = int(input(task_menu).strip()) 
        return choice


class File : 
    def __init__(self ) -> None:
        self.ReadData()
    
    def ReadData (self) : 
        with open ("data.json",mode='r') as file : 
            self.data=json.load(file)
    def saveData (self) : 
        with open ("data.json",mode='w') as file : 
            json.dump(self.data , file ,indent=4)


    

if __name__ == "__main__" : 
    menu = Menu() 
    data =File()
    task = Task(data=data.data)
    task.show_tasks()
    while True :
        clean_screen()
        task.show_tasks()
        choice=menu.Task_menu()
        if choice == 1 : 
            clean_screen()
            task.Add_Task()

        elif choice == 2 :
            clean_screen() 
            task.mark_task_as_complete_or_incomplete()

        elif choice == 3 :
            clean_screen() 
            task.Task_Note()


        elif choice == 4 : 
            clean_screen()
            task.Remove_Task()
        
        elif choice == 5 :
            data.data =task.tasks
            data.saveData()
            task.Quit()
        
        else : 
            # clean_screen()
            print ("Error, Please Enter Valid Choice") 
            time.sleep(2)
    
