from django.contrib.auth.models import User
from django import forms
from authentication.models import Account

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
        first_name = self.cleaned_data['firstname']
        if (
                not (first_name.isalnum() or first_name.isalpha())
        ):
            raise forms.ValidationError("Name contains invalid characters")
        return first_name


    def clean_lastname(self):
        last_name = self.cleaned_data['lastname']
        if (
                not (last_name.isalnum() or last_name.isalpha())
        ):
            raise forms.ValidationError("Name contains invalid characters")
        return last_name


class Edit_profile2(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['phonenumber','city','country', 'adress', 'state']
        widgets = {
            'phonenumber' : forms.TextInput({'required':'required','placeholder':'Phonenumber'}),
            'city' : forms.TextInput({'required':'required','placeholder':'City'}),
            'country' : forms.TextInput({'required':'required','placeholder':'Country'}),
            'adress': forms.TextInput({'required': 'required', 'placeholder': 'Country'}),
            'state': forms.TextInput({'required': 'required', 'placeholder': 'Country'})
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

    def clean_country(self):
        country = self.cleaned_data['country']
        if country.isalpha == False:
            raise forms.ValidationError("Country name contains invalid characters")
        return country

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