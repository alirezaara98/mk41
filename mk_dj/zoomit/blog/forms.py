from blog.models import Comment
from django.forms.widgets import PasswordInput
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class user_reg_form(forms.Form):
    username = forms.CharField(label=_('username'), max_length=150)
    first_name = forms.CharField(label=_('first_name'))
    last_name = forms.CharField(label=_('last_name'))
    mail = forms.EmailField(label=_('email'), help_text='<br>!!use valid email address', required=True)
    password = forms.CharField(label=_('password'),widget= PasswordInput, required=True)
    password_repeat = forms.CharField(label=_('password_repeat'),widget= PasswordInput , required=True)

    def clean(self):
        password = self.cleaned_data.get('password', None)
        password_repeat = self.cleaned_data.get('password_repeat', None)
        if password_repeat != password:
            raise ValidationError(_('password doesn\'t match'), code= 'invalid')

    def clean_username(self):
        username = self.cleaned_data.get('username', None)
        try:
            User.objects.get(username= username)
            raise ValidationError(_("this username already exist"), code='invalid')
        except User.DoesNotExist:
            pass
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', None)
        if len(password)< 8:
            raise ValidationError(_('password id too short'), code='invalid')
        return password 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {'content': _('comment')}
        help_texts = {'content': _('enter your comment')}
        widgets = {'content': forms.Textarea}
        