from django.contrib import admin
from contents.models import (
    Content,
    User
)


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "uuid",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined"
    ]


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "content",
        "status",
        "review_notes",
        "created_at",
        "modified_at"
    ]
