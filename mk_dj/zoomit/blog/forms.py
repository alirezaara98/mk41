from django import forms
from django.utils.translation import ugettext_lazy as _
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {'content': _('comment')}
        help_texts = {'content': _('enter your comment')}
        widgets = {'content': forms.Textarea}


# class CommentLikeForm(forms.Form):
#     status = forms.CharField()
#     comment = forms.IntegerField()
#
#     def clean_status(self):
#         status = self.cleaned_data['status']
#         return status == 'true'