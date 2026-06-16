from django import forms
from django.contrib.auth.models import User
from . import models

class ContactusForm(forms.Form):
    Name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control contact-input',
            'placeholder': 'Your full name',
            'autocomplete': 'name',
        }),
    )
    Email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control contact-input',
            'placeholder': 'you@example.com',
            'autocomplete': 'email',
        }),
    )
    Message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': 'form-control contact-input contact-textarea',
            'rows': 5,
            'placeholder': 'Write your message here...',
        }),
    )


class CategoryForm(forms.ModelForm):
    class Meta:
        model=models.Category
        fields=['category_name']

class PolicyForm(forms.ModelForm):
    category=forms.ModelChoiceField(queryset=models.Category.objects.all(),empty_label="Category Name", to_field_name="id")
    class Meta:
        model=models.Policy
        fields=['policy_name','sum_assurance','premium','tenure']

class QuestionForm(forms.ModelForm):
    class Meta:
        model=models.Question
        fields=['description']
        widgets = {
        'description': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }