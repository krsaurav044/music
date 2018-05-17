from django.shortcuts import render,get_object_or_404
from .models import Playlist,song
from django.http import HttpResponseRedirect,Http404
from django.contrib import messages
from .forms import AddForm
from urllib.parse import quote

# Create your views here.
def addsong(request):
	form=AddForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"successfully added")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request,"not successfully added")
	if request.method=="POST":
		print(request.POST.get("album_name"))
		print(request.POST.get("song_name"))
	context={
	    "form":form,
	}
	return render(request,"forms.html",context)

def desplay(request,id):
	track=song.objects.get(id=id)
	#album=Playlist.objects.get(id=id)
	context={
	"track":track,
	#"album":album,

	}
	return render(request,"play.html",context)


def songslist(request):
	album_list=Playlist.objects.all()
	track_list=song.objects.all()
	query=request.GET.get("q")
	if query:
		track_list=track_list.filter(song_name__icontains=query)
		
	context={
	    "track_list":track_list,
	    "album_list":album_list,
	}
	return render(request,"list.html",context)

def albumdisplay(request,id):
	albm=Playlist.objects.get(id=id)
	trk_list=song.objects.filter(album_id=id)
	context={
	   "albm":albm,
	   "trk_list":trk_list,
	}
	return render(request,'album.html',context)

def editsong(request,id=None):
	instance=get_object_or_404(song,id=id)
	form=AddForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"<a href='#'>Item</a> saved",extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
	"song_name":instance.song_name,
	"instance":instance,
	"form":form,
	}
	return render(request,"forms.html",context)
