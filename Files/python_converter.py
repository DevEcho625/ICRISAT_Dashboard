import pandas as pd
#import geopandas as gpd
import openpyxl
import json

xlf = pd.read_excel("/home/anujbhatia/django-projects/ICRISAT_Dashboard/maps/dashboard/data/FLDREQ2013.xlsx")
values = json.loads(xlf.to_json(orient='records'))
value_by_field = {}
for val in values:
    value_by_field[val["FIELDNO"]] = val
print(value_by_field)
# gdf = gpd.read_file("final.shp")
# gdf.to_file("/tmp/final.json", driver="GeoJSON")
