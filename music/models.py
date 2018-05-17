from django.db import models

# Create your models here.
def upload_location(instance,filename):
	return "%s/%s" %(instance.id,filename)

class Playlist(models.Model):
	album_name=models.CharField(max_length=30)
	date=models.DateTimeField(auto_now=False, auto_now_add=True)
	albumart=models.ImageField(upload_to=upload_location)



	def get_absolute_url1(self):
		return "/songs/list/%s" %(self.id)

	def __str__(self):
		return self.album_name



class song(models.Model):
	song_name=models.CharField(max_length=30)
	audio_file=models.FileField(upload_to=upload_location)
	song_image=models.ImageField(upload_to=upload_location,default=True)
	album=models.ForeignKey('Playlist',on_delete=models.CASCADE,default=True)


	def get_absolute_url(self):
		return "/songs/%s" %(self.id)