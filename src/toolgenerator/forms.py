from django import forms


class GenerateAdhocFileForm(forms.Form):

    names = forms.CharField(label='Your name', max_length=23)
    types = forms.MultipleChoiceField(label='Your name', widget=forms.CheckboxSelectMultiple)

    # class Meta:
    #
    #     fields = ['types', 'env']