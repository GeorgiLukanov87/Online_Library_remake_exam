from django.shortcuts import render, redirect

from Online_Library_remake_exam.my_web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, \
    BookCreateForm, BookEditForm
from Online_Library_remake_exam.my_web.models import ProfileModel, BookModel


def get_profile():
    return ProfileModel.objects.first()


def get_all_books():
    return BookModel.objects.all().order_by('id')


def get_current_book(pk):
    return BookModel.objects.filter(pk=pk).get()


def index(request):
    profile = get_profile()
    books = get_all_books()

    if not profile:
        return redirect('create-profile')

    context = {'books': books, 'profile': profile, }
    return render(request, 'common/home-with-profile.html', context, )


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
    profile = get_profile()
    context = {'profile': profile, }
    return render(request, 'profile/details-profile.html', context, )


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {'profile': profile, 'form': form, }

    return render(request, 'profile/edit-profile.html', context, )


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'profile': profile, 'form': form, }
    return render(request, 'profile/delete-profile.html', context)


# Books views:
def add_book(request):
    profile = get_profile()
    if request.method == 'GET':
        form = BookCreateForm()
    else:
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, 'profile': profile, }

    return render(request, 'book/add-book.html', context, )


def edit_book(request, pk):
    profile = get_profile()
    book = get_current_book(pk)

    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('details-book', pk)

    context = {'form': form, 'book': book, 'profile': profile, }

    return render(request, 'book/edit-book.html', context, )


def delete_book(request, pk):
    book = get_current_book(pk)
    book.delete()
    return redirect('index')


def details_book(request, pk):
    profile = get_profile()
    book = get_current_book(pk)
    context = {'book': book, 'profile': profile, }
    return render(request, 'book/book-details.html', context, )
