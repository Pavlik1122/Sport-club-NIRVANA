from django.forms import ModelForm

from mainapp.models import Feedback


class MailForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Выберите абонемент: '
        self.fields['full_name'].widget.attrs['placeholder'] = 'ФИ: '
        self.fields['tel'].widget.attrs['placeholder'] = 'Телефон: '
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail: '
        for field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            field.label = ''
