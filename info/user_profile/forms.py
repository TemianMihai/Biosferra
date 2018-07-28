from django.contrib.auth.models import User
from django import forms
from authentication.models import Account2, Account
from .models import Message, Report, Favourite, Profile

class Edit_profile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput({'required': 'required',
                                         'placeholder': 'Username'}),
            'email': forms.EmailInput({'required': 'required',
                                       'placeholder': 'Email'}),

            'first_name': forms.TextInput({'required': 'required',
                                         'placeholder': 'First Name'}),
            'last_name': forms.TextInput({'required': 'required',
                                         'placeholder': 'Last Name'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Edit_profile, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email) and self.user.email != email:
            raise forms.ValidationError("This email already exists")
        return email

    def clean_username(self):
        user_name = self.cleaned_data['username']
        if User.objects.filter(username=user_name).count() and \
                        self.user.username != user_name:
            raise forms.ValidationError("This username already exists")
        return user_name

    def clean_firstname(self):
        first_name = self.cleaned_data['first_name']
        if (
                not (first_name.isalnum() or first_name.isalpha())
        ):
            raise forms.ValidationError("Name contains invalid characters")
        return first_name


    def clean_lastname(self):
        last_name = self.cleaned_data['last_name']
        if (
                not (last_name.isalnum() or last_name.isalpha())
        ):
            raise forms.ValidationError("Name contains invalid characters")
        return last_name


class Edit_profile_buyer(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['phonenumber','city', 'adress', 'state']
        widgets = {
            'phonenumber' : forms.TextInput({'required':'required','placeholder':'Phonenumber'}),
            'city' : forms.TextInput({'required':'required','placeholder':'City'}),
            'adress': forms.TextInput({'required': 'required', 'placeholder': 'Country'}),
            'state': forms.TextInput({'required': 'required', 'placeholder': 'Country'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Edit_profile_buyer, self).__init__(*args, **kwargs)

    def clean_phonenumber(self):
        phone_number = self.cleaned_data['phonenumber']
        if phone_number[0] != '0' or phone_number[1] != '7' or len(phone_number) != 10 or phone_number.isdigit() == False:
            raise forms.ValidationError("Invalid phonenumber")
        return phone_number

    def clean_city(self):
        city = self.cleaned_data['city']
        if city.isalpha == False:
            raise forms.ValidationError("City name contains invalid characters")
        return city

    def clean_adress(self):
        adress = self.cleaned_data['adress']
        if adress.isalpha == False:
            raise forms.ValidationError("Adress name contains invalid characters")
        return adress

    def clean_state(self):
        state = self.cleaned_data['state']
        if state.isalpha == False:
            raise forms.ValidationError("State name contains invalid characters")
        return state


class Edit_profile2(forms.ModelForm):
    class Meta:
        model = Account2
        fields = ['phonenumber','city', 'adress', 'state', 'file1', 'file2']
        widgets = {
            'phonenumber' : forms.TextInput({'required':'required','placeholder':'Phonenumber'}),
            'city' : forms.TextInput({'required':'required','placeholder':'City'}),
            'adress': forms.TextInput({'required': 'required', 'placeholder': 'Country'}),
            'state': forms.TextInput({'required': 'required', 'placeholder': 'Country'}),
            'file1': forms.FileInput({'required':'required', 'placeholder': 'Country'}),
            'file2': forms.FileInput({'required':'required', 'placeholder': 'Country'})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Edit_profile2, self).__init__(*args, **kwargs)

    def clean_phonenumber(self):
        phone_number = self.cleaned_data['phonenumber']
        if phone_number[0] != '0' or phone_number[1] != '7' or len(phone_number) != 10 or phone_number.isdigit() == False:
            raise forms.ValidationError("Invalid phonenumber")
        return phone_number

    def clean_city(self):
        city = self.cleaned_data['city']
        if city.isalpha == False:
            raise forms.ValidationError("City name contains invalid characters")
        return city

    def clean_adress(self):
        adress = self.cleaned_data['adress']
        if adress.isalpha == False:
            raise forms.ValidationError("Adress name contains invalid characters")
        return adress

    def clean_state(self):
        state = self.cleaned_data['state']
        if state.isalpha == False:
            raise forms.ValidationError("State name contains invalid characters")
        return state

    def clean_file1(self):
        file1 = self.cleaned_data['file1']
        if file1.size > 5242880:
            raise forms.ValidationError("Imaginile sunt prea mari")
        return file1

    def clean_file2(self):
        file2 = self.cleaned_data['file2']
        if file2.size > 5242880:
            raise forms.ValidationError("Imaginile sunt prea mari")
        return file2

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['product1', 'product2', 'product3', 'product4', 'product5', 'description', 'profile_image',
                  'cover_image', ]
        widgets = {
            'product1': forms.TextInput({'required': 'required', 'placeholder': 'Produs din gradina dumneavoastra'}),
            'product2': forms.TextInput({'required': 'required', 'placeholder': 'Produs din gradina dumneavoastra'}),
            'product3': forms.TextInput({'required': 'required', 'placeholder': 'Produs din gradina dumneavoastra'}),
            'product4': forms.TextInput({'required': 'required', 'placeholder': 'Produs din gradina dumneavoastra'}),
            'product5': forms.TextInput({'required': 'required', 'placeholder': 'Produs din gradina dumneavoastra'}),
            'description': forms.TextInput({'required': 'required', 'placeholder': 'Descriere'}),
            'profile_image': forms.FileInput({'required': 'required', 'placeholder': 'Country'}),
            'cover_image': forms.FileInput({'required': 'required', 'placeholder': 'Country'})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateProfileForm, self).__init__(*args, **kwargs)

    def clean_product1(self):
        produs1 = self.cleaned_data['product1']
        return produs1

    def clean_product2(self):
        produs2 = self.cleaned_data['product2']
        return produs2

    def clean_product3(self):
        produs3 = self.cleaned_data['product3']
        return produs3

    def clean_product4(self):
        produs4 = self.cleaned_data['product4']
        return produs4

    def clean_product5(self):
        produs5 = self.cleaned_data['product5']
        return produs5

    def clean_description(self):
        descriere = self.cleaned_data['description']
        return descriere

    def clean_cover_image(self):
        image1 = self.cleaned_data['profile_image']
        image2 = self.cleaned_data['cover_image']
        image_names = []
        if (image1 and not isinstance(image1, (int, float))):
            image_names.append(image1.name)
        if (image2 and not isinstance(image2, (int, float))):
            image_names.append(image2.name)
        if (len(image_names) - 1 == len(set(image_names))):
            raise forms.ValidationError("You can't upload 2 images"
                                        "that are the same")
        return image2


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['product1', 'product2', 'product3', 'product4', 'product5', 'description']
        widgets = {
            'product1': forms.TextInput({'required': 'required', 'placeholder': 'Produs1'}),
            'product2': forms.TextInput({'required': 'required', 'placeholder': 'Produs2'}),
            'product3': forms.TextInput({'required': 'required', 'placeholder': 'Produs3'}),
            'product4': forms.TextInput({'required': 'required', 'placeholder': 'Produs4'}),
            'product5': forms.TextInput({'required': 'required', 'placeholder': 'Produs4'}),
            'description': forms.TextInput({'required': 'required', 'placeholder': 'Descriere'}),

        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EditProfileForm, self).__init__(*args, **kwargs)

    def clean_product1(self):
        produs1 = self.cleaned_data['product1']
        return produs1

    def clean_product2(self):
        produs2 = self.cleaned_data['product2']
        return produs2

    def clean_product3(self):
        produs3 = self.cleaned_data['product3']
        return produs3

    def clean_product4(self):
        produs4 = self.cleaned_data['product4']
        return produs4

    def clean_product5(self):
        produs5 = self.cleaned_data['product5']
        return produs5

    def clean_description(self):
        descriere = self.cleaned_data['description']
        return descriere


class CreateMesajeForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'title']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateMesajeForm, self).__init__(*args, **kwargs)

    def clean_mesaj(self):
        mesaj = self.cleaned_data['content']
        return mesaj

    def clean_titlu(self):
        titlu = self.cleaned_data['title']
        return titlu


class CreateReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['content', 'title']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateReportForm, self).__init__(*args, **kwargs)

    def clean_mesaj(self):
        mesajj = self.cleaned_data['content']
        return mesajj

    def clean_titlu(self):
        titluu = self.cleaned_data['title']
        return titluu


class CreateFavoritForm(forms.ModelForm):
    class Meta:
        model = Favourite
        fields = []

    def  __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateFavoritForm, self).__init__(*args, **kwargs)
