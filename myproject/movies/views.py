from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django.http import HttpResponse

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

def home(request):
    return HttpResponse("Welcome to the Movies API!")