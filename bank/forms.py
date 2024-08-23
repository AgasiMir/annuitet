from django import forms


class PercentForm(forms.Form):
    money = forms.IntegerField(
        label="Размер вклада", initial=100_000, min_value=10_000, max_value=10_000_000
    )
    year = forms.IntegerField(
        label="Срок вклада в годах",
        initial=5,
        min_value=1,
        max_value=10,
        help_text="Срок вклада: от одного года до десяти лет включительно",
    )
    percent = forms.IntegerField(label="Процент", initial=6, disabled=True)
    phone = forms.RegexField(
        label="Номер телефона",
        regex=r"\+7 \d{3} \d{3} \d{2} \d{2}",
        initial="+7",
        max_length=16,
    )
