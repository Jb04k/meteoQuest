from django.shortcuts import render
from .forms import CityForm

# Dummy weather data function (replace with real API call)
def get_weather(city_name):
    return {
        'city': city_name,
        'temperature': 22,  # Example temperature
        'description': 'clear sky',
        'icon': '01d',
    }

def index(request):
    form = CityForm()
    weather = {}
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['name']
            weather = get_weather(city)
    context = {
        'form': form,
        'weather': weather,
    }
    return render(request, "meteo/index.html", context)

def doodle_game(request):
    return render(request, "meteo/doodle.html")

def reaction_game(request):
    return render(request, "meteo/reaction.html")

def puzzle_game(request):
    return render(request, "meteo/puzzle.html")
