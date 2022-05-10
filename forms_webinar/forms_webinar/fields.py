from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RussianNameField(forms.CharField):
    def to_python(self, value):
        """
        Преобразовываем данные в Python-строку или в None
        """
        return value

    def validate(self, value):
        """
        Проверим, что используются только буквы
        русского алфавита и имя с большой буквы
        """
        russian_chars = [
            chr(i) for i in range(ord('А'), ord('я')+1)
        ] + ['Ё', 'ё', '-']
        if len(value) < 2:
            raise ValidationError(
                _('%(value) короче двух символов'),
                params={'value': value}
            )
        if value.startswith('-') or value.endswith('-'):
            raise ValidationError(
                _('%(value) не может начинаться или заканчиваться на дефис'),
                params={'value': value}
            )
        if set(value).difference(russian_chars):
            raise ValidationError(
                _(
                    '%(value) должно содержать только буквы русского алфавита'
                    'и знак дефиса'
                ),
                params={'value': value}
            )
