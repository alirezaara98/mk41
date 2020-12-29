# from django.forms.widgets import PasswordInput
from django.utils.translation import ugettext_lazy as _
from django import forms
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class user_reg_form(forms.Form):
    # username = forms.CharField(label=_('username'), max_length=150,
    #                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(label=_('full_name'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField(label=_('email'), widget=forms.EmailInput(attrs={'class': 'form-control'}),
                            help_text='!!use valid email address', required=True)
    password1 = forms.CharField(label=_('password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                required=True)
    password2 = forms.CharField(label=_('password_repeat'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

    def clean(self):
        password1 = self.cleaned_data.get('password', None)
        password2 = self.cleaned_data.get('password_repeat', None)
        if password2 != password1:
            raise ValidationError(_('password doesn\'t match'), code='invalid')

    # def clean_username(self):
    #     username = self.cleaned_data.get('username', None)
    #     try:
    #         User.objects.get(username=username)
    #         raise ValidationError(_("this username already exist"), code='invalid')
    #     except User.DoesNotExist:
    #         pass
    #     return username

    def clean_password(self):
        password = self.cleaned_data.get('password1', None)
        if len(password) < 8:
            raise ValidationError(_('password id too short'), code='invalid')
        return password
