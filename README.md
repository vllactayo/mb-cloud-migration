# MapBiomas Perú - Cloud Migration

This guidelines document outlines the process of migrating assets associated with the generation of land cover and land use maps for MapBiomas Peru, from local storage (Legacy Assets) to Google Cloud Storage. The development team carried out this migration using a standardized structure and optimized code to streamline the process. As a result, scripts, vector layers, raster data, and classification products were successfully migrated for the three main initiatives: MapBiomas LULC, MapBiomas AGUA, and MapBiomas Wetlands.

## Google Cloud Structure

La nueva estructura en el repositorio de Google Cloud fue rediseñada pensando en la replicabilidad, orden intuitivo y estandarizado de las carpetas. Se definieron principalmente tres niveles principales tal como se muestra en la Figura 1. Estos niveles siguen ciertas características como las siguientes:

The new Google Cloud Structure was redesigned with replicability, intuitive order and standarized folder organization in mind. We primarily defined three levels as shown in Figure 1. These levels follow specific characteristics, such as the following:

* The names of the main level folders must be in english and written in uppercase
* Image Collection, tables and raster names must be in lowercase
* Each initiative must have an Auxiliary-data folder to store rasters files, vectors and statistics

## Workflow and step by step process


