from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Client name', required=True, max_length=15)
    age = forms.IntegerField(label='Client age', required=False, max_value=99, min_value=14)
    # презаполнение поля за пользователя
    social_url = forms.URLField(label='Your social profile', initial='https://')
    remember = forms.BooleanField(label='Remember me', initial=True)  # по умолчанию галочка будет нажата
    # ip_address = forms.GenericIPAddressField(label='IP address', protocol='IPv4')
    date = forms.DateField(widget=forms.SelectDateWidget(years=range(1970, 2030)))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    # поле с паролем скрывает символы, которые вы в него пишете

