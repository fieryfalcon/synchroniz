

# Register your models here.
from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    """
    Custom admin class for the custom user model
    """
    fields = ('email', 'password', 'is_active',)
    list_display = ('email', 'is_active',)
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)