# Script de download Sentinel-2 para sudoeste do Paraná
import ee
import geemap
import os


# Inicialização
# Assuma que o usuário autenticou: 'earthengine authenticate'
ee.Authenticate()
ee.Initialize(project='hidden-pad-271403')


# Coordenadas aproximadas do sudoeste do Paraná (polígono exemplo) — ajuste conforme necessário
poly = ee.Geometry.Polygon([
    [-52.8, -26.4],
    [-52.8, -26.2],
    [-52.6, -26.2],
    [-52.6, -26.4],
])


def mask_s2_clouds(image):
    qa = image.select('QA60')
    cloud_bit_mask = 1 << 10
    cirrus_bit_mask = 1 << 11
    mask = (
        qa.bitwiseAnd(cloud_bit_mask).eq(0)
        .And(qa.bitwiseAnd(cirrus_bit_mask).eq(0))
    )
    return image.updateMask(mask).divide(10000)


# Seleciona coleção Sentinel-2 Level-2A (correção atmosférica aplicada)
collection = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED') \
    .filterBounds(poly) \
    .filterDate('2020-01-01', '2020-01-30') \
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)) \
    .map(mask_s2_clouds)


# Função de máscara de nuvem usando SCL (Scene classification layer)


def mask_s2_sr(image):
    scl = image.select('SCL')
    # Valores que indicam nuvens: 3 = vegetação baixa? (exemplo). Filtre 3, 8, 9, 10 (valores de nuvem e sombras)
    mask = scl.neq(3).And(scl.neq(8)).And(scl.neq(9)).And(scl.neq(10))
    return image.updateMask(mask)


# Aplicar a máscara de nuvem
visualization = {
    'min': 0.0,
    'max': 0.3,
    'bands': ['B4', 'B3', 'B2'],
}

m = geemap.Map()
m.set_center(-52.7, -26.2, 10)  # sudoeste do Paraná
m.add_layer(collection.mean(), visualization, 'RGB')
m


collection = collection.map(mask_s2_sr)


# Criar mosaico mediano e normalizar (B02,B03,B04,B08 são úteis)
bands = ['B2', 'B3', 'B4', 'B8']
median = collection.select(bands).median().clip(poly)


# Exportar para Google Drive / Assets ou baixar com geemap
out_dir = 'data/tiles'
os.makedirs(out_dir, exist_ok=True)


# Usando geemap para baixar um GeoTIFF local (atenção às quotas)
path = os.path.join(out_dir, 'sentinel2_median_SW_Para.tif')
geemap.ee_export_image(median, filename=path, scale=30,
                       region=poly, file_per_band=False)
print('Exportado para', path)
