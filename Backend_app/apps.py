from django.apps import AppConfig
from . import signals

class BackendAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Backend_app'

class UsersConfig(AppConfig):
    name = 'Backend_app'

    def ready(self):
        import signals
