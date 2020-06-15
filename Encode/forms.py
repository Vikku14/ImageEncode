from django import forms
from .models import ImageData


class ImageForm(forms.ModelForm):

    class Meta:
        model = ImageData
        fields=('photo','base64_format', 'hash_format')
        widgets = {'base64_format': forms.HiddenInput(),
                    'hash_format': forms.HiddenInput()
                    }
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['base64_format'].required = False
        self.fields['hash_format'].required = False
