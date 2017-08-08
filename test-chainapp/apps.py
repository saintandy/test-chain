from django.apps import AppConfig


class DemoAppConfig(AppConfig):
    name = "test-chainapp"

    def ready(self):
        pass