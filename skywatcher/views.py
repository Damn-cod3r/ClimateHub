from django.shortcuts import render
import requests
from django.conf import settings
from .models import Weather  # Import the Weather model

def index(request):
    # Access the API key from settings
    api_key = settings.WEATHER_API_KEY

    # Default city (if no input is provided)
    city = request.GET.get('city', 'London')

    # OpenWeatherMap API URL (with the city and API key)
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    # Fetch data from the API
    response = requests.get(url)
    weather_data = response.json()

    # Prepare the context for the template
    context = {}
    if weather_data.get('cod') == 200:
        # Extract data from the API response
        city_name = weather_data['name']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        humidity = weather_data['main']['humidity']
        icon = weather_data['weather'][0]['icon']

        # Save data to the database
        Weather.objects.create(
            city=city_name,
            temperature=temperature,
            description=description,
            wind_speed=wind_speed,
            humidity=humidity,
            icon=icon
        )

        # Pass data to the template
        context = {
            'city': city_name,
            'temperature': temperature,
            'weather_description': description,
            'wind_speed': wind_speed,
            'humidity': humidity,
            'icon': icon,
        }
    else:
        context = {
            'error': 'City not found. Please try again.'
        }

    # Render the template with the weather information
    return render(request, 'skywatcher/index.html', context)



def history(request):
    weather_history = Weather.objects.all().order_by('-date_searched')  # Show recent first
    return render(request, 'skywatcher/history.html', {'weather_history': weather_history})
