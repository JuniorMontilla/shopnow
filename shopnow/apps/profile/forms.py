from django import forms

class loginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class registerform(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email  = forms.EmailField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class  profileform(forms.Form):
    CHOICES=[('mujer','mujer'),('hombre','hombre')]

    avatar       =  forms.ImageField()
    phone        =  forms.CharField(widget=forms.TextInput())
    cellphone    =  forms.CharField(widget=forms.TextInput())
    address     =  forms.CharField(widget=forms.TextInput())
    sex          =  forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    dateofbirth  =  forms.DateField(widget=forms.DateInput())
    occupation   =  forms.CharField(widget=forms.TextInput())
    country      =  forms.CharField(widget=forms.TextInput())
    city         =  forms.CharField(widget=forms.TextInput())
    province     =  forms.CharField(widget=forms.TextInput())
    municipality =  forms.CharField(widget=forms.TextInput())
