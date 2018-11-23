from django.contrib import admin

# Register your models here.
from .models import Game, Rule, FAQ
admin.site.register(Game)
admin.site.register(Rule)
admin.site.register(FAQ)