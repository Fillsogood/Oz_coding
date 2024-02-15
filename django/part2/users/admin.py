from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    #admin.ModelAdmin
    # list_display = ["name","description","age","gender"]
    # list_filter = ["age","gender"]
    # search_fields = ["name"]
    
    # UserAdmin
    list_display = ("username", "email", "is_business","grade")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}), 
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )