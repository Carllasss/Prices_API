from django import forms


class PriceForm(forms.Form):
    order = forms.CharField()
    price_usa = forms.DecimalField()
    price_rus = forms.DecimalField()
    delivery_date = forms.DateTimeField()
