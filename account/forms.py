from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control fields', 'autocomplete': 'off',
               'placeholder': 'Username'}
    ))
    fullname = forms.CharField(label='Fullname', widget=forms.TextInput(
        attrs={'class': 'form-control fields', 'autocomplete': 'off',
               'placeholder': 'Fullname'}
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control fields', 'autocomplete': 'off', 'placeholder': 'Email'}
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control fields', 'autocomplete': 'off', 'id': 'password',
               'placeholder': 'Password'}
    ))

    class meta:
        fields = ['username', 'email', 'password', 'fullname']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control fields', 'autocomplete': 'off',
               'placeholder': 'Username'}
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control fields', 'autocomplete': 'off', 'id': 'password',
               'placeholder': 'Password'}
    ))

    class meta:
        fields = ['username', 'email']