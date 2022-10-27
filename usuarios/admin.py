from django.contrib import admin
from .models import Users
from django.contrib import admin
from django.contrib.auth import admin as admin_auth_django 
from .forms import UserChangeForm, UserCreationform

# Register your models here.
@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationform
    model = Users 
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}),
    )#type:ignore