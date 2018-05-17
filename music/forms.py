from django import forms
from .models import Playlist,song
class AddForm(forms.ModelForm):
	class Meta:
		model=song
		fields=[
		   "song_name",
	       "audio_file",
	       'song_image',
	       "album",

	]