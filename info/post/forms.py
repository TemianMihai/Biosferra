from django import forms
from django.core.validators import validate_email
from .models import PostModel, Comment, CosulMeu, AdresaDeFacturare, Comanda, CHOICES_UM, CHOICES_SEASON
from category.models import Category
from categorie.models import Categorie
from lfcat.models import Products
from django.shortcuts import get_object_or_404

class FilterForm(forms.Form):
    sort_by = forms.ChoiceField(label="Sorteaza dupa", choices=(
        (0, "Autor"),
        (1, "Pret crescator"),
        (2, "Pret descrescator")
    ), widget=forms.RadioSelect, required=False)
    products = forms.ModelMultipleChoiceField(label="Produse", queryset=Products.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    um = forms.ChoiceField(choices=CHOICES_UM, label="Unitate de masura", widget=forms.RadioSelect, required=False)
    min_quantity = forms.IntegerField(label="Minq", required=False)
    max_quantity = forms.IntegerField(required=False, label="Maxq")
    min_price = forms.IntegerField(required=False, label="Minp")
    max_price = forms.IntegerField(required=False, label="Maxp")

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['name', 'quantity', 'price', 'details', 'image1', 'image2', 'image3', 'image4', 'season', 'um', 'product_type']
        widgets = {
            'image1': forms.FileInput({'required': 'required', 'placeholder': "Image1"}),
            'image2': forms.FileInput({'required': 'required', 'placeholder': "Image2"}),
            'image3': forms.FileInput({'required': 'required', 'placeholder': "Image3"}),
            'image4': forms.FileInput({'required': 'required', 'placeholder': "Image4"})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreatePostForm, self).__init__(*args, **kwargs)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price.isdigit() == False:
            raise forms.ValidationError("Pret invalid")
        return price

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.isdigit():
            raise forms.ValidationError("Numele contine caractere invalide")
        return name

    def clean_details(self):
        details = self.cleaned_data['details']
        return details

    def clean_image4(self):
        image1 = self.cleaned_data['image1']
        image2 = self.cleaned_data['image2']
        image3 = self.cleaned_data['image3']
        image4 = self.cleaned_data['image4']
        image_names = []
        if (image1 and not isinstance(image1, (int, float))):
            image_names.append(image1.name)
        if (image2 and not isinstance(image2, (int, float))):
            image_names.append(image2.name)
        if (image3 and not isinstance(image3, (int, float))):
            image_names.append(image3.name)
        if (image4 and not isinstance(image4, (int, float))):
            image_names.append(image4.name)
        if (len(image_names) - 1 == len(set(image_names))):
            raise forms.ValidationError("Imaginile trebuie sa fie diferite")
        if image1._size > 5242880:
            raise forms.ValidationError("Imaginile sunt prea mari")
        if image2._size > 5242880:
            raise forms.ValidationError("Imaginile sunt prea mari")
        if image3._size > 5242880:
            raise forms.ValidationError("Imaginile sunt prea mari")
        if image4._size > 5242880:
            raise forms.ValidationError("Imaginile sunt prea mari")
        return image4

    def clean_um(self):
        um = self.cleaned_data['um'] if self.cleaned_data['um'] in [i[0] for i in CHOICES_UM] else None
        if um is None:
            raise forms.ValidationError("Unitate de masura invalida")
        return um

    def clean_season(self):
        print([i[0] for i in CHOICES_SEASON])
        season = self.cleaned_data['season'] if self.cleaned_data['season'] in [i[0] for i in CHOICES_SEASON] else None
        if season is None:
            raise forms.ValidationError("Anotimp invalid")
        return season

    def clean_product_type(self):
        product_type = get_object_or_404(Products,
                                         name=self.cleaned_data['product_type'])
        return product_type

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("Cantitate invalida")
        return quantity


class DeleteNewForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = []


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class CreateCosForm(forms.ModelForm):
    class Meta:
        model = CosulMeu
        fields = []

    def  __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateCosForm, self).__init__(*args, **kwargs)


class CreateComandaForm(forms.ModelForm):
    class Meta:
        model = AdresaDeFacturare
        fields = ['nume','prenume','email','nrdetelefon','adresa','judet','localitate','codpostal','nume2','prenume2','adresa2','judet2','localitate2','codpostal2','comentarii']
        widgets = {
            'nume': forms.TextInput({'required': 'required', 'placeholder': "Nume"}),

            'prenume': forms.TextInput({'required': 'required', 'placeholder': "Prenume"}),

            'email': forms.TextInput({'required': 'required', 'placeholder': "Email"}),

            'nrdetelefon': forms.TextInput({'required': 'required', 'placeholder': "Numar de telefon"}),

            'adresa': forms.TextInput({'required': 'required', 'placeholder': "Adresa"}),

            'judet': forms.TextInput({'required': 'required', 'placeholder': "Judet"}),

            'localitate': forms.TextInput({'required': 'required', 'placeholder': "Localitate"}),

            'codpostal': forms.TextInput({'required': 'required', 'placeholder': "Cod Postal"}),

            'nume2': forms.TextInput({'required': 'required', 'placeholder': "Nume"}),

            'prenume2': forms.TextInput({'required': 'required', 'placeholder': "Prenume"}),

            'adresa2': forms.TextInput({'required': 'required', 'placeholder': "Adresa"}),

            'judet2': forms.TextInput({'required': 'required', 'placeholder': "Judet"}),

            'localitate2': forms.TextInput({'required': 'required', 'placeholder': "Localitate"}),

            'codpostal2': forms.TextInput({'required': 'required', 'placeholder': "Cod Postal"}),

            'comentarii': forms.TextInput({'placeholder': "Comentarii"})
        }

    def  __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateComandaForm, self).__init__(*args, **kwargs)

    def clean_nume(self):
        nume = self.cleaned_data['nume']
        if nume.isdigit():
            raise forms.ValidationError("Numele contine caractere invalide")
        return nume

    def clean_prenume(self):
        prenume = self.cleaned_data['prenume']
        if prenume.isdigit():
            raise forms.ValidationError("Prenumele contine caractere invalide")
        return prenume

    def clean_email(self):
        email = self.cleaned_data['email']
        if validate_email(email):
            raise forms.ValidationError("Emailul nu e valid")
        return email

    def clean_nrdetelefon(self):
        nrdetelefon = self.cleaned_data['nrdetelefon']
        if nrdetelefon[0] != '0' or nrdetelefon[1] != '7' or len(nrdetelefon) != 10 or nrdetelefon.isdigit() == False:
            raise forms.ValidationError("Numarul de telefon e invalid")
        return nrdetelefon

    def clean_adresa(self):
        adresa = self.cleaned_data['adresa']
        return adresa

    def clean_judet(self):
        judet = self.cleaned_data['judet']
        if judet.isdigit():
            raise forms.ValidationError("Judetul contine caractere invalide")
        return judet

    def clean_localitate(self):
        localitate = self.cleaned_data['localitate']
        if localitate.isdigit():
            raise forms.ValidationError("Localitatea contine caractere invalide")
        return localitate

    def clean_codpostal(self):
        codpostal = self.cleaned_data['codpostal']
        if codpostal.isdigit() == False or len(codpostal) != 6:
            raise forms.ValidationError("Codul postal contine caractere invalide")
        return codpostal

    def clean_nume2(self):
        nume2 = self.cleaned_data['nume2']
        if nume2.isdigit():
            raise forms.ValidationError("Numele contine caractere invalide")
        return nume2

    def clean_prenume2(self):
        prenume2 = self.cleaned_data['prenume2']
        if prenume2.isdigit():
            raise forms.ValidationError("Prenumele contine caractere invalide")
        return prenume2

    def clean_adresa2(self):
        adresa2 = self.cleaned_data['adresa2']
        return adresa2

    def clean_judet2(self):
        judet2 = self.cleaned_data['judet2']
        if judet2.isdigit():
            raise forms.ValidationError("Judetul contine caractere invalide")
        return judet2

    def clean_localitate2(self):
        localitate2 = self.cleaned_data['localitate2']
        if localitate2.isdigit():
            raise forms.ValidationError("Localitatea contine caractere invalide")
        return localitate2

    def clean_codpostal2(self):
        codpostal2 = self.cleaned_data['codpostal2']
        if codpostal2.isdigit() == False or len(codpostal2) != 6:
            raise forms.ValidationError("Codul postal contine caractere invalide")
        return codpostal2

    def clean_comentarii(self):
        comentarii = self.cleaned_data['comentarii']
        return comentarii


class PlaseazaComandaForm(forms.ModelForm):
    class Meta:
        model = Comanda
        fields = []

    def  __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PlaseazaComandaForm, self).__init__(*args, **kwargs)
