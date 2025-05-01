from django import forms
from django.core.exceptions import ValidationError
from .models import DDSEntry



class DDSEntryForm(forms.ModelForm):
    class Meta:
        model = DDSEntry
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        subcategory = cleaned_data.get("subcategory")
        entry_type = cleaned_data.get("type")

        # Проверка: Категория должна относиться к выбранному типу
        if category and entry_type and category.type != entry_type:
            raise ValidationError("Категория не принадлежит выбранному типу!")

        # Проверка: Подкатегория должна относиться к выбранной категории
        if subcategory and category and subcategory.category != category:
            raise ValidationError("Подкатегория не принадлежит выбранной категории!")

        return cleaned_data