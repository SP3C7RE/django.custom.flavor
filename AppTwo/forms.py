from django import forms
from AppTwo.models import User
from django.core import validators


class UsersForm(forms.ModelForm):
        class Meta:
            model = User
            fields = "__all__"
            # fields = ('firstName','lastName','email')

            
        # def clean(self):
        #     all_clean_data = super().clean()
        #     firstName = all_clean_data['firstName']
        #     lastName = all_clean_data['lastName']
        #     email = all_clean_data['email']
        #
