from django.shortcuts import render, redirect

from Online_Library_remake_exam.my_web.forms import ProfileCreateForm
from Online_Library_remake_exam.my_web.models import ProfileModel


def get_profile():
    return ProfileModel.objects.first()


def index(request):
    profile = get_profile()

    if not profile:
        return redirect('create-profile')

    return render(request, 'common/home-with-profile.html')


# Profile views:
def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, }
    return render(request, 'profile/create-profile.html', context, )


def details_profile(request):
    return render(request, 'profile/details-profile.html')


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')


# Books views:
def add_book(request):
    return render(request, 'book/add-book.html')


def edit_book(request, pk):
    return render(request, 'book/edit-book.html')


def details_book(request, pk):
    return render(request, 'book/book-details.html')


def delete_book(request, pk):
    pass
