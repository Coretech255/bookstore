from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

#get the user active model and assign it CustomerUser
CustomUser = get_user_model()

#create a custom user admin class
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username',]

admin.site.register(CustomUser, CustomUserAdmin)



