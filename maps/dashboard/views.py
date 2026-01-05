
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import random
from datetime import date, timedelta

def map_view(request):
    return render(request, "dashboard/map.html")

def field_data(request, field_id):
    crops = ["Sorghum", "Millet", "Chickpea", "Maize", "Pigeon Pea"]

    data = {
        "field_id": field_id,
        "crop": random.choice(crops),
        "last_fertilized": str(date.today() - timedelta(days=random.randint(10, 60))),
        "last_sown": str(date.today() - timedelta(days=random.randint(30, 120))),
        "soil_moisture": f"{random.randint(20, 60)}%",
        "nitrogen_level": f"{random.randint(30, 90)} kg/ha",
        "expected_yield": f"{random.uniform(1.2, 3.8):.2f} tons/ha"
    }

    return JsonResponse(data)
