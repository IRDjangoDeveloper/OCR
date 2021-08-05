from django import forms
country_choice =(
    ("fas", "فارسی"),
    ("eng", "English"),
    ("ara", "Arabic"),
    ("deu", "German"),
    ("urd", "اردو"),
    ("fra", "French"),
    ("hin", "Hindi"),
    ("hin", "Hindi"),
    ("jpn", "Japanese"),
    ("kor", "Korean"),
    ("ita", "Italian"),
    ("tgk", "Tajik"),
    ("pus", "Pashto"),
)
class imageForm(forms.Form):
    lang = forms.ChoiceField(choices=country_choice, widget=forms.Select(attrs={'class':'form-control'}), label='language')
    img = forms.ImageField(label='Picture')

class textinput(forms.Form):
    content = forms.Textarea()