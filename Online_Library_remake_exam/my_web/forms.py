from django import forms

from Online_Library_remake_exam.my_web.models import ProfileModel, BookModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL'
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL'
                }
            ),


        }


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass
