from django.forms import ValidationError


def validate_brilliant(value):
    must_words = ('превосходно', 'роскошно')
    if (must_words[0] or must_words[1]) not in value.lower():
        raise ValidationError(
            f'Вы должны использовать слово {must_words[0]} или {must_words[1]}')


def validate_more_than_2(value):
    if len(value.split()) < 2:
        raise ValidationError('Должно содержать минимум 2 слова')
