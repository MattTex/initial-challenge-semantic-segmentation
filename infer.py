# Inferência e geração de GeoTIFF/GeoJSON
import profile
import rasterio
from rasterio.features import shapes
import geopandas as gpd
import numpy as np
import shapely


# suponha `mask` seja numpy 2D com 0/1
with rasterio.open('data/masks/sentinel2_median_SW_Para.tif') as src:
    mask = src.read(1)  # lê a primeira banda
mask = np.where(mask > 0, 1, 0)  # binariza a máscara
# affine transform from raster
transform = rasterio.Affine(1, 0, 0, 0, -1, mask.shape[0])
profile = {
    'driver': 'GTiff',
    'dtype': 'uint8',
    'nodata': 0,
    'width': mask.shape[1],
    'height': mask.shape[0],
    'count': 1,
    'crs': 'EPSG:4326',
    'transform': transform
}

results = []
for geom, val in shapes(mask.astype('uint8'), transform=transform):
    if val == 1:
        results.append(geom)


gdf = gpd.GeoDataFrame(
    {'geometry': [shapely.geometry.shape(g) for g in results]}, crs='EPSG:4326')


# salvar
gdf.to_file('results/exports/runways.geojson', driver='GeoJSON')
gdf.to_file('results/exports/runways.shp')  # shapefile
with rasterio.open('results/exports/runways.tif', 'w', **profile) as dst:
    dst.write(mask.astype('uint8'), 1)
