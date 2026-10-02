from django import forms
from .models import QuoteRequest, Service

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name','phone','email','service','message','website']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Your name','autocomplete':'name'}),
            'phone': forms.TextInput(attrs={'placeholder':'+971 ...','autocomplete':'tel'}),
            'email': forms.EmailInput(attrs={'placeholder':'you@company.com','autocomplete':'email'}),
            'service': forms.Select(attrs={'class':'js-service-select'}, choices=[]),
            'message': forms.Textarea(attrs={'placeholder':'Tell us briefly about your requirement','rows':5}),
            'website': forms.TextInput(attrs={'tabindex':'-1','autocomplete':'off','class':'hp-field','aria-hidden':'true'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = [('', 'Select a service')]
        choices += list(Service.objects.values_list('name','name'))
        self.fields['service'].widget.choices = choices
        self.fields['website'].required = False
    def clean_website(self):
        value = self.cleaned_data.get('website','')
        if value: raise forms.ValidationError('Spam detected.')
        return value
