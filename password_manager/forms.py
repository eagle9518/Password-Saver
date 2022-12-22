from django import forms

from password_manager.models import Site


class NewCategoryForm(forms.Form):
    category = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Category Name'}),
                               max_length=256)


class NewPasswordForm(forms.ModelForm):

    class Meta:
        model = Site
        fields = ['site', 'username', 'password']
