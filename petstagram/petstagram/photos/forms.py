from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from petstagram.common.models import Like, Comment
from petstagram.photos.models import Photo

UserModel = get_user_model()


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'user')


class PhotoCreateForm(PhotoBaseForm):
    ...


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo')


class PhotoDeleteForm(PhotoBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for (name, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            Like.objects.filter(to_photo_id=self.instance.id).delete()
            Comment.objects.filter(to_photo_id=self.instance).delete()
            self.instance.delete()
        return self.instance

    # def clean_tagged_pets(self):
    #     tagged_pets = self.cleaned_data['tagged_pets']
    #     if tagged_pets:
    #         raise ValidationError("Pets are tagged")
