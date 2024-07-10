import json
from pathlib import Path

from barberq.models import Barber, User

DATA_DIR = Path(__file__).parent / 'data'


def run():
    with open(DATA_DIR / 'barbers.json', 'r', encoding='utf-8') as f:
        barbers = json.load(f)

    for barber in barbers:
        try:
            user = User(**barber, password='BarberQ123!')
            user.clean_fields()
            user.save()
            user.refresh_from_db()
            Barber.objects.create(user=user)
        except Exception:
            print(f'Failed to create user: {barber["username"]}')

    print('Done!')
