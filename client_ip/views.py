from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .utils import get_client_ip


# Create your views here.

class HelloView(APIView):
    def get(self, request):
        visitor_name = request.GET.get("visitor_name", "Dear HNG intern")
        client_ip = get_client_ip(request)
        location = "Nairobi, Kenya"
        
        api_key = 'd2ee0201f418cf0685bbf1422db050ca'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}'

        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()
            temperature = weather_data['main']['temp']
        except (requests.RequestException, KeyError) as e:
            temperature = "unavailable"

        greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"

        data = {
            'client_ip': client_ip,
            'location': location,
            'greeting': greeting
        }

        return Response(data, status=status.HTTP_200_OK)
    