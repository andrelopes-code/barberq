from datetime import datetime, timezone

from barberq.models import (
    Barber,
    Client,
    Reservation,
    ReservationStatusEnum,
    Service,
    User,
)
from django.test import TestCase


class TestModelsCreation(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='Test User',
            phone='123456789',
            bio='Test bio',
            password='password',
            email='a@a.com',
        )

    def test_user_creation(self):
        user = User.objects.get(username=self.user.username)
        assert user
        assert str(user) == self.user.username
        assert user.bio == 'Test bio'
        assert user.phone == '123456789'

    def test_barber_creation(self):
        barber = Barber.objects.create(user=self.user)
        assert barber
        assert str(barber) == self.user.username
        assert barber.user.username == self.user.username
        assert Barber.objects.count() == 1

    def test_client_creation(self):
        client = Client.objects.create(user=self.user)
        assert client
        assert str(client) == self.user.username
        assert client.user.username == self.user.username
        assert Client.objects.count() == 1

    def test_reservation_creation(self):
        reservation = Reservation.objects.create(
            barber=Barber.objects.create(user=self.user),
            client=Client.objects.create(user=self.user),
            notes='Test notes',
            date=datetime.now(timezone.utc),
            status=ReservationStatusEnum.PENDING,
        )
        assert reservation
        assert reservation.barber.user.username == self.user.username
        assert reservation.client.user.username == self.user.username
        assert Reservation.objects.count() == 1

    def test_service_creation(self):
        service = Service.objects.create(name='Test Service', price=10.0)
        assert self
        assert service
        assert str(service) == 'Test Service'
        assert service.name == 'Test Service'
        assert service.price == 10.0  # noqa
        assert Service.objects.count() == 1
