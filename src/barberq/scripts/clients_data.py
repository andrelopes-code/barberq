import json
from pathlib import Path

from barberq.models import Client, User

DATA_DIR = Path(__file__).parent / 'data'


def run():
    with open(DATA_DIR / 'clients.json', 'r', encoding='utf-8') as f:
        clients = json.load(f)

    for client in clients:
        try:
            user = User(**client, password='BarberQ123!')
            user.clean_fields()
            user.save()
            user.refresh_from_db()
            Client.objects.create(user=user)
        except Exception:
            print(f'Failed to create user: {client["username"]}')

    print('Done!')
