from django import forms

from temp_project.web.mixins import DisabledFormMixin
from temp_project.web.models import TestProfile


class ProfileCreateForm(DisabledFormMixin, forms.ModelForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self._disable_fields()

    class Meta:
        model = TestProfile
        fields = '__all__'
