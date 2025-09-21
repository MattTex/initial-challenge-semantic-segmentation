# Visualização interativa dos resultados
import folium
import geopandas as gpd
from folium import GeoJson


m = folium.Map(location=[-26.0, -52.0], zoom_start=9)
# adicionar basemap via WMS ou tiles do sentinel
# overlay GeoJSON
g = gpd.read_file('results/exports/runways.geojson')
GeoJson(g.__geo_interface__).add_to(m)
m.save('results/exports/map_runways.html')
