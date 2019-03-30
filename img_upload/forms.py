from django import forms
from django.core.files.storage import default_storage


class UploadForm(forms.Form):
    file = forms.FileField(label='ファイル')

    def save(self):
        upload_file = self.files['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)


# forms.py
class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )
    class Meta:
        model = Image
        fields = ('image',)
