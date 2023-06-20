from django.contrib import admin

from Online_Library_remake_exam.my_web.models import ProfileModel, BookModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type',)
