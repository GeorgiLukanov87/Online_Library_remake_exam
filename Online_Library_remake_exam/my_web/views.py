from django.shortcuts import render, redirect


def index(request):
    profile = None

    if not profile:
        return redirect('create-profile')

    return render(request, 'common/home-with-profile.html')


# Profile views:
def create_profile(request):
    return render(request, 'profile/create-profile.html')


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
