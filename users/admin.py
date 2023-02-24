from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm   
    list_filter = ("is_staff", "is_active", "is_superuser", "validate")
    list_display = ("username", "full_name", "user_status", "checkVerify", "last_login")

    def user_status(self, obj):
        if obj.is_active == True and obj.is_superuser == True:
            return "Superuser"
        elif obj.is_active == True and obj.is_staff == True:
            return "Admin"
        elif obj.is_active == False:
            return "Userni accounti vaqtinchalik blocklangan"
        else:
            return "User sozlamalari to'liq ko'rsatilmagan"
    
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
    def checkVerify(self, obj):
        return "Validated" if obj.validate else "Not validated"

    fieldsets = (
        ("Shaxsiy malumotlar", {
            "fields": (
                "first_name", 
                "last_name", 
                "phone",
                "email",
                ),
            },
        ),
        ("Asosiy malumotlar", {
            "classes": ("collapse",),
            "fields": (
                "username", 
                "password",
                "validate_code"
                )
            }
        ),
        ("Ruxsatlar", {
            "classes": ("collapse",),
            "fields": (
                "is_active", 
                "is_staff", 
                "is_superuser",
                "validate", 
                "groups", 
                "user_permissions"
                ),
            }
        ),
        ("Vaqt", {
            "classes": ("collapse",),
            "fields": (
                "last_login", 
                "date_joined"
                )
            }
        ),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "is_staff", "is_active")}
         ),
    )