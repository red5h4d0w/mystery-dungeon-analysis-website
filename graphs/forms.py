from django import forms


class FiltersForm(forms.Form):
    min_asc = forms.IntegerField(label="Minimum ascension level:", initial=0, widget=forms.NumberInput( attrs={'type':'range', 'step': '1', 'min': '0', 'max': '20', "onchange":"this.form.submit()", "oninput":"this.nextElementSibling.value = this.value"}), required=False)
    max_asc = forms.IntegerField(label="Maximum ascension level:", initial=20, widget=forms.NumberInput( attrs={'type':'range', 'step': '1', 'min': '0', 'max': '20', "onchange":"this.form.submit()", "oninput":"this.nextElementSibling.value = this.value"}), required=False)
    only_show_upgrades = forms.BooleanField(label="Show data only for upgraded cards:", initial=False, widget=forms.CheckboxInput(attrs={"onchange":"this.form.submit()"}), required=False)
    only_show_wins = forms.BooleanField(label="Show data only for runs won:", initial=False, widget=forms.CheckboxInput(attrs={"onchange":"this.form.submit()"}), required=False)