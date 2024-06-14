from django import forms
from .models import BulletinPost


class BulletinPostForm(forms.ModelForm):
    class Meta:
        model = BulletinPost
        fields = ('title', 'content')
