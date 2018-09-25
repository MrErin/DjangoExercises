from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, FormView, DetailView, CreateView
from history.models import Artist, Song, Album, Genre


class IndexView(TemplateView):
    """Creates view for index"""

    template_name = "history/index.html"

    # ?Not sure what location is for?

    def location(self):
        return 'home'


class ArtistListTemplateView(TemplateView):
    template_name = 'history/artists.html'

    def artist_list(self):
        artists = Artist.objects.all()
        return artists


class ArtistDetailView(DetailView):
    model = Artist


class SongListView(ListView):
    model = Song
    context_object_name = 'song_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = "songs"
        return context


class SongDetailView(DetailView):
    model = Song
