from django.core import validators

# Phone number field validator
phone_number = [
    validators.RegexValidator(
        r'^\d{11}$',
        'Phone number must be 11 digits long. e.g. 11988888888',
    ),
]


# Password field validator
password = [
    validators.RegexValidator(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        message='Password must be at least 8 characters long and contain at'
        ' least one uppercase letter, one lowercase letter, one number and one'
        ' special character. e.g. P@ssw0rd!',
    ),
]
