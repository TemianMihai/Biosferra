from django.test import TestCase
from django.contrib.auth.models import User
from .forms import CreateProfileForm, CreateReportForm
from .models import Profile, Report
# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='omcaretesteaza',password='cevaparola',email='wtf@wtf.com')
        self.user.save()

        self.user2 = User.objects.create_user(username='omcaretesteaza2',password='cevaparola2',email='wtf@wtf2.com')
        self.user2.save()

        self.profil = Profile.objects.create(user=self.user, product1='mere', product2='para',
                                            product3='visine', product4='cartofi', product5='rosii',
                                            description='alabalaportocala', cover_image='tests/tests2.png',
                                            profile_image='tests/tests')
        self.profil.save()

        self.report = Report.objects.create(autor=self.user, mesajj="wtf is wrong", titluu='report', destinatar=self.user2, slug='sadsadsadsasddsds')
        self.report.save()

    def test_create_profile_invalid_form(self):
        produs1 = self.profil.produs1
        form_data = Profile.objects.get(produs1=produs1)
        form = CreateProfileForm(instance=form_data)
        self.assertFalse(form.is_valid())

    def test_create_report_invalid_form(self):
        mesaj = self.report.mesajj
        form_data = Report.objects.get(mesajj=mesaj)
        form = CreateReportForm(instance=form_data)
        self.assertFalse(form.is_valid())
