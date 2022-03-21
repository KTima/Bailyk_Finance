from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import *
from django.forms import ModelForm,DateInput


class CardForm(ModelForm):
    class Meta:
        model = CardData
        fields = ['Status']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))


class CreateForm(ModelForm):
    class Meta:
        model = Create
        fields = ['Series','kolvo']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))