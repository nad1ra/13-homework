from django.shortcuts import render, redirect, get_object_or_404
from .models import Track

def home(request):
    return render(request, 'index.html')


def track_list(request):
    musics = Track.objects.all()
    ctx = {'musics': musics}
    return render(request, 'tracks/music-list.html', ctx)


def track_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        release_date = request.POST.get('release_date')
        image = request.POST.get('image')
        audio = request.POST.get('audio')
        if (title and artist and album and genre and
        release_date and image and audio):
            Track.objects.create(
                title=title,
                artist=artist,
                album=album,
                genre=genre,
                release_date=release_date,
                image=image,
                audio=audio
            )
            return redirect('tracks:list')
    return render(request, 'tracks/music-list.html')


def track_detail(request, pk):
    track = get_object_or_404(Track, pk=pk)
    ctx = {'track': track}
    return render(request, 'tracks/music-detail.html', ctx)


def track_update(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        release_date = request.POST.get('release_date')
        image = request.POST.get('image')
        audio = request.POST.get('audio')
        if (title and artist and album and genre and release_date
            and image and audio):
            track.title=title
            track.artist=artist
            track.album=album
            track.genre=genre
            track.release_date=release_date
            track.image=image
            track.audio=audio
            track.save()
            return redirect(track.get_detail_url())
    ctx = {'track', track}
    return render(request,'tracks/music-update.html', ctx)


def track_delete(pk):
    track = get_object_or_404(Track, pk=pk)
    track.delete()
    return redirect('tracks:list')

