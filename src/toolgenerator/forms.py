from django import forms
from django.core import validators

# from django import MultipleChoiceField, ChoiceField, Form

class GenerateAdhocFileForm(forms.Form):
    DEMO_CHOICES = (
        ("1", "Naveen"),
        ("2", "Pranav"),
        ("3", "Isha"),
        ("4", "Saloni"),
    )

    namess = forms.MultipleChoiceField(required=False, choices=DEMO_CHOICES)
    # ex_weekends = forms.CharField(label='Your name', required=False, max_length=23)
    # date_range = forms.CharField(label='Your name', max_length=50, required=False)
    # types = forms.CharField(label='Your name', required=False)
    # portfolios = forms.MultipleChoiceField(label='Your name', widget=forms.CheckboxSelectMultiple, required=False)
    # stress_model = forms.MultipleChoiceField(label='Your name', widget=forms.CheckboxSelectMultiple, required=False)
    # mcvar_model = forms.MultipleChoiceField(label='Your name', widget=forms.CheckboxSelectMultiple, required=False)
    # headlines_model = forms.MultipleChoiceField(label='Your name', widget=forms.CheckboxSelectMultiple, required=False)
    # headline_assets_model = forms.MultipleChoiceField(label='Your name', widget=forms.CheckboxSelectMultiple, required=False)

    # class Meta:
    #
    #     fields = ['types', 'env']