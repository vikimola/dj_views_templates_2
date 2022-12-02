from django.forms import ModelForm, TextInput
from .models import Pet, Owner


class PetForm(ModelForm):
    class Meta:
        model = Pet
        # fields = ["name", "race", "owner_name", "leg_number", "do_we_like", "age"]
        fields = '__all__'



class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        # fields = ["name", "do_we_like", "date_of_birth", "other_observations"]
        fields = '__all__'
        widgets = {
            'other_observations': TextInput(attrs={
                # 'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Other observations',
                'padding': '10px',

            })}