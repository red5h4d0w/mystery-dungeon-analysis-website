from django import forms
from .models import Game


class FiltersForm(forms.Form):
    min_asc = forms.IntegerField(label="Minimum ascension level:", initial=0, widget=forms.NumberInput( attrs={'type':'range', 'step': '1', 'min': '0', 'max': '20', "onchange":"this.form.submit()", "oninput":"this.nextElementSibling.value = this.value"}), required=False)
    max_asc = forms.IntegerField(label="Maximum ascension level:", initial=20, widget=forms.NumberInput( attrs={'type':'range', 'step': '1', 'min': '0', 'max': '20', "onchange":"this.form.submit()", "oninput":"this.nextElementSibling.value = this.value"}), required=False)
    only_show_upgrades = forms.BooleanField(
        label="Show data only for upgraded cards:", 
        initial=False, 
        widget=forms.CheckboxInput(attrs={"onchange":"this.form.submit()"}), 
        required=False
    )
    only_show_wins = forms.BooleanField(
        label="Show data only for runs won:", 
        initial=False, 
        widget=forms.CheckboxInput(attrs={"onchange":"this.form.submit()"}), 
        required=False
    )
    minimum_version = forms.ChoiceField(
        label="minimum version:", 
        choices=map(lambda v: (f"v{v//100**2}.{v//100%100}.{v%100}",f"v{v//100**2}.{v//100%100}.{v%100}"),
            map(lambda v: v[0], list(Game.objects.values_list("version").distinct()))
        ), 
        required=False
    )
    max_version = forms.ChoiceField(
        label="maximum version", 
        choices=map(lambda v: (f"v{v//100**2}.{v//100%100}.{v%100}",v),
            map(lambda v: v[0], list(Game.objects.values_list("version").distinct()))
        ), 
        required=False
    )