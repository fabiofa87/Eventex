from django import forms


def validate_cpf(value):
    if not value.isdigit():
        raise forms.ValidationError('CPF deve conter apenas números', 'digits')
    elif len(value) != 11:
        raise forms.ValidationError('CPF deve ter 11 números', 'length')



class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(label='Telefone')