from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render


def home(request: HttpRequest):
    return render(request, 'barberq/index.html')


@login_required
def reservation(request: HttpRequest):
    return render(request, 'barberq/reservation.html')
