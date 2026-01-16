
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from datetime import date, timedelta
from pathlib import Path
from django.conf import settings
from django.http import JsonResponse
from pathlib import Path
from django.conf import settings

import logging
import pandas as pd
import random
import json

logger = logging.getLogger(__name__)

EXCEL_PATH = Path(settings.BASE_DIR) / "dashboard" / "data" / "FLDREQ2013.xlsx"

def load_excel():
    logging.info('In load_excel')
    xlfstr = pd.read_excel(EXCEL_PATH).to_json(orient='records')
    values = json.loads(xlfstr)
    # convert array to dictionary based on field no
    field_info = {}
    for val in values:
        field_info[val["FIELDNO"]] = val
        logging.info("Got field: {}".format(val["FIELDNO"]))
    return field_info

FIELD_INFO = load_excel()


# Normalize column names (important)
def map_view(request):
    return render(request, "dashboard/map.html")

def field_data(request, field_id):
    logging.info('In field_data')
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

def fields_geojson(request):
    logging.info('In fields_geojson')
    geojson_path = Path(settings.BASE_DIR) / "dashboard" / "data" / "final.json"

    with open(geojson_path) as f:
        data = json.load(f)

    return JsonResponse(data)

def map_view(request):
    logging.info('In map_view')
    return render(request, "dashboard/map.html")


def field_details(request, field_no):
    logging.info('In Field Details for {}'.format(field_no))
    if field_no not in FIELD_INFO:
        logging.info("Field {} not found".format(field_no))
        return JsonResponse({
            "error": "Field not found",
            "requested": field_no,
        })
    row = FIELD_INFO[field_no]
    logging.info("Got field info: {}".format(row))
    return JsonResponse(row)

