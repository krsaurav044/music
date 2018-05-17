from django.contrib import admin

# Register your models here.
from .models import Playlist,song
# Register your models here.
admin.site.register(Playlist)
admin.site.register(song)