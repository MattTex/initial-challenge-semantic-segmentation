# Pré-processamento da imagem Sentinel-2
import rasterio
import numpy as np
from rasterio.enums import Resampling


def compute_indices(arr):
    # arr shape: (bands, H, W) ordered [B2,B3,B4,B8]
    b2, b3, b4, b8 = arr
    ndvi = (b8 - b4) / (b8 + b4 + 1e-6)
    # NDBI aprox com b11 se disponível. Aqui apenas exemplo com b4 como proxy
    return ndvi


with rasterio.open('data/tiles/sentinel2_median_SW_Para.tif') as src:
    arr = src.read().astype('float32')
    # normalize per-band
    for i in range(arr.shape[0]):
        band = arr[i]
        arr[i] = (band - band.min()) / (band.max() - band.min() + 1e-6)

ndvi = compute_indices(arr)
# salvar indices como novo TIFF se desejar
