from django import forms
from datetime import date
from .models import PostModel
from django.shortcuts import get_object_or_404

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['name', 'delivery_time', 'cantity', 'price', 'details', 'image1']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreatePostForm, self).__init__(*args, **kwargs)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price.isdigit() == False:
            raise forms.ValidationError("Invalid price")
        return price

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.isdigit():
            raise forms.ValidationError("Name contains invalid characters")
        return name

    def clean_details(self):
        details = self.cleaned_data['details']
        return details

    def clean_image1(self):
        image1 = self.cleaned_data['image1']
        image_names = []
        if (image1 and not isinstance(image1, (int, float))):
            image_names.append(image1.name)
        return image1

    def clean_cantity(self):
        cantity = self.cleaned_data['cantity']
        if cantity.isdigit() == False:
            raise forms.ValidationError("Invalid cantity")
        return cantity

    def clean_deliverytime(self):
        delivery_time = self.cleaned_data['delivery_time']
        if delivery_time.isdigit() == False:
            raise forms.ValidationError("Invalid delivery time")
        return delivery_time