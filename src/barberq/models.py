from barberq.utils import validators
from django.contrib.auth.models import AbstractUser
from django.db import models


class ReservationStatusEnum(models.IntegerChoices):
    # Enum class for the reservation status
    CONFIRMED = 1, 'Confirmed'
    CANCELLED = 2, 'Cancelled'
    PENDING = 3, 'Pending'


# The User model is where the Barber and Client models are linked.
# It extends the default django User model.
class User(AbstractUser):
    phone = models.CharField(max_length=11, validators=validators.phone_number)
    bio = models.TextField(null=True, blank=True)


# Represents a barber who is associated with a user.
class Barber(models.Model):
    # This field links the Barber model to the default django User model.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


# Represents a client who is associated with a user.
class Client(models.Model):
    # This field links the Client model to the default django User model.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


# Represents a booking made by a client with a barber.
class Reservation(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    status = models.IntegerField(
        choices=ReservationStatusEnum.choices,
        default=ReservationStatusEnum.PENDING,
    )


# Represents a service offered by a barber.
class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
