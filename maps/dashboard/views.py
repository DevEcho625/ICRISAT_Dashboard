
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import random
from datetime import date, timedelta
from pathlib import Path
import json
from django.conf import settings
import pandas as pd
from django.http import JsonResponse
from pathlib import Path
from django.conf import settings



EXCEL_PATH = Path(settings.BASE_DIR) / "dashboard" / "data" / "FLDREQ2013.xlsx"

def load_excel():
    path = Path(settings.BASE_DIR) / "dashboard" / "data" / "FLDREQ2013.xlsx"
    return pd.read_excel(path)

df = load_excel()


# Normalize column names (important)
df.columns = df.columns.str.strip()
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

def fields_geojson(request):
    geojson_path = Path(settings.BASE_DIR) / "dashboard" / "data" / "final.json"

    with open(geojson_path) as f:
        data = json.load(f)

    return JsonResponse(data)

def map_view(request):
    return render(request, "dashboard/map.html")


def field_details(request, field_no):
    # Normalize spreadsheet FIELDNO
    df["FIELDNO"] = df["FIELDNO"].astype(str).str.strip()

    # Normalize incoming value
    field_no = str(field_no).strip()

    row = df[df["FIELDNO"] == field_no]

    if row.empty:
        return JsonResponse({
            "error": "Field not found",
            "requested": field_no,
            "available_sample": df["FIELDNO"].head(10).tolist()
        })

    row = row.iloc[0]

    return JsonResponse({
        "FIELDNO": row["FIELDNO"],
        "REQNO": row.get("REQNO", ""),
        "DATEPTD": str(row.get("DATEPTD", "")),
        "PLANTDATE": str(row.get("PLANTDATE", "")),
        "HARVESTDAT": str(row.get("HARVESTDAT", "")),
        "ACTUALPDAT": str(row.get("ACTUALPDAT", "")),
        "EXPDETAIL": row.get("EXPDETAIL", ""),
        "PESTNAME": row.get("PESTNAME", ""),
        "HERBNAME": row.get("HERBNAME", "")
    })