from django import forms


class PriceForm(forms.Form):
    order = forms.CharField()
    price_usa = forms.IntegerField()
    price_rus = forms.FloatField()
    delivery_date = forms.DateTimeField()
