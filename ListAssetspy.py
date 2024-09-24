#install GEE

import ee

ee.Authenticate()

ee.Initialize(project = 'ee-coberturaibc3')

import pandas as pd

#INTRODUCIR LA RUTA DE LA CARPETA QUE DESEAS LISTAR
asset_path = "projects/mapbiomas-raisg/MAPBIOMAS-PERU/COLECCION3/TRANSVERSALES/PLAYAS/clasificacion-ft"

asset_list = ee.data.listAssets(asset_path)

#print(asset_list)

# Dic to DF
assets = asset_list['assets']

df_assets = pd.DataFrame(assets)

ee_assets = df_assets.drop('name', axis=1)
ids = ee_assets['id']

# Convertir los valores a una lista
ids_list = [f'"{id}"' for id in ids]

ids_string = ', '.join(ids_list)

print(ids_string) # COPIAR ESTA LISTA AL SCRIPT

# Exportar to excel (OPCIONAL)
#ee_assets.to_excel("assets-COL3-VECTOR.xlsx", index=False)
#MANIPULAR EL DF (SI SE DESEA COMPARTIR COMO XLSX)
delete = asset_path + '/'

ee_assets['asset'] = ee_assets['id'].apply(lambda x: x.replace(delete, ''))

ee_assets.head(1)
ids = ee_assets['asset']

# Convertir los valores a una lista
ids_list = [f'"{id}"' for id in ids]

ids_string = ', '.join(ids_list)

print(ids_string) # COPIAR ESTA LISTA AL SCRIPT