# forms.py
from django import forms
from .models import MenuPortions

class MenuPortionsForm(forms.ModelForm):
    class Meta:
        model = MenuPortions
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        menu_name = cleaned_data.get('menu_name')
        item_name = cleaned_data.get('item_name')

        if MenuPortions.objects.filter(menu_name=menu_name, item_name=item_name).exclude(id=self.instance.id).exists():
            existing_item = MenuPortions.objects.get(menu_name=menu_name, item_name=item_name)
            raise forms.ValidationError(f"The item '{existing_item.item_name}' already exists for this menu.")
        
        return cleaned_data
