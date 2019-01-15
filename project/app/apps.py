from django.apps import AppConfig

class AppConfig(AppConfig):
    name = 'app'
    
    def ready(self):
        # Load our receivers
        # This is important as receiver hooks are not connected otherwise.
        from . import receivers

class GrouperConfig(AppConfig):
    name = 'grouper'
