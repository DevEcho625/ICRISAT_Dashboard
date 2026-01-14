import geopandas as gpd

gdf = gpd.read_file("final.shp")
gdf.to_file("final.json", driver="GeoJSON")
