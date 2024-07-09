from django.apps import AppConfig


class BarberqConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'barberq'

    def ready(self):  # noqa
        import barberq.templatetags.custom_filters  # noqa
