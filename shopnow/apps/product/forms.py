from django import forms
from shopnow.apps.product.models import product

class productform(forms.ModelForm):
    class Meta:
        model = product
        exclude = {'status','username'}     
