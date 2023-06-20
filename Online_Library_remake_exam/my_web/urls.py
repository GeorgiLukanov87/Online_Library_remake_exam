from django.urls import path, include

from Online_Library_remake_exam.my_web.views import index, add_book, edit_book, details_book, delete_book, \
    details_profile, create_profile, edit_profile, delete_profile

urlpatterns = (
    path('', include([
        path('', index, name='index'),
        path('add/', add_book, name='add-book'),
        path('edit/<int:pk>/', edit_book, name='edit-book'),
        path('details/<int:pk>/', details_book, name='details-book'),
        path('delete/<int:pk>/', delete_book, name='delete-book'),
    ])),

    path('profile/', include([
        path('', details_profile, name='details-profile'),
        path('create/', create_profile, name='create-profile'),
        path('edit/', edit_profile, name='edit-profile'),
        path('delete/', delete_profile, name='delete-profile'),
    ])),
)

"""

http://localhost:8000/ - home page

http://localhost:8000/add/ - add book page
http://localhost:8000/edit/1 - edit book page
http://localhost:8000/details/1 - book details page
additional
http://localhost:8000/delete/1 - book delete page

http://localhost:8000/profile/ -  details profile page
http://localhost:8000/profile/edit/ - edit profile page
http://localhost:8000/profile/delete/ - delete profile page
additional
http://localhost:8000/profile/create/ - create profile page

"""
