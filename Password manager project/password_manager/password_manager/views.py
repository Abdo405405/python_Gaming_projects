from django.http import HttpResponse 
from django.shortcuts import render 

import json

def main_page(request) : 

    return render (request , "main_page.html")


def load_add_password_page(request) : 

    if request.method == "POST" : 
       account_name = request.POST.get("account_name")
       password =  request.POST.get("password")
       add_new_password({f"{account_name}":f"{password}"})
       return render (request , "main_page.html")



    return render (request , "add_page.html")
    



def load_view_passwords_page (request) :
    context = {}
    rows=display_passwords()
    context["data"] = zip(rows ,range(1,len(rows)+1))
    return render (request , "view_passwords.html" ,context)




def add_new_password (new_data)  : 
    data = {}
    with open (r"F:\Python\Password manager project\password_manager\password_manager\passwords.json" , mode='r' ) as json_file : 
        try : 
            data = json.load(json_file)
            data["password"].append(new_data)

        except json.JSONDecodeError as e: 
            # IF Error here is raised That maen the file is empty so we put default data 
            data["password"] = []

 
    with open (r"F:\Python\Password manager project\password_manager\password_manager\passwords.json" , mode='w' ) as json_file :
        json.dump(data , json_file ,indent=4) 



def display_passwords () : 
    data = {}
    with open (r"F:\Python\Password manager project\password_manager\password_manager\passwords.json" , mode='r' ) as json_file : 
        try : 
            data = json.load(json_file)["password"]

        except json.JSONDecodeError as e: 
            # IF Error here is raised That maen the file is empty so we put default data 
            data["password"] = []


    return data
    