
from django.contrib import admin
from django.urls import path
from . import views

app_name = "myapp" 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("" , view=views.main_page , name="main_page") , 
    path("add_page/" , view=views.load_add_password_page , name="add_page"),
    path("view_page/" , view=views.load_view_passwords_page , name="view_page")

    
]

