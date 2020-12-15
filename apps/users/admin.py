from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Notification


@admin.register(User)
class UserAdmin(UserAdmin):
    pass

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass
