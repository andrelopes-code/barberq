from django.core import validators

# Phone number field validator
phone_number = [
    validators.RegexValidator(
        r'^\d{11}$',
        'O número de telefone deve conter 11 dígitos. e.g. 11988888888',
        code='invalid_phone_number',
    ),
]


# Password field validator
password = [
    validators.RegexValidator(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        message='A senha deve conter pelo menos 8 dígitos,'
        ' pelo menos uma letra maiúscula, pelo menos uma letra minúscula,'
        ' pelo menos um número e pelo menos um caractere especial.',
        code='invalid_password',
    ),
]
