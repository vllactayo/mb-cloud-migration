# MapBiomas Perú - Cloud Migration 🌎☁️

This guidelines document outlines the process of migrating assets associated with the generation of land cover and land use maps for MapBiomas Peru, from local storage (Legacy Assets) to Google Cloud Storage. The development team carried out this migration using a standardized structure and optimized code to streamline the process. As a result, scripts, vector layers, raster data, and classification products were successfully migrated for the three main initiatives: MapBiomas LULC, MapBiomas AGUA, and MapBiomas Wetlands.

## Google Cloud Structure ☁️

The new Google Cloud Structure was redesigned with replicability, intuitive order and standarized folder organization in mind. We primarily defined three levels as shown in Figure 1. These levels follow specific characteristics, such as the following:

* ✅The names of the main level folders must be in english and written in uppercase 
* ✅Image Collection, tables and raster names must be in lowercase
* ✅Each initiative must have an Auxiliary-data folder to store rasters files, vectors and statistics

![Figure 1. New Folder structure and folder levels](https://github.com/vllactayo/mb-cloud-migration/blob/main/gc-folder-levels.png)

## Workflow and step by step process ⚙️

The migration process began with the assignment of responsible individuals and editors for each repository by country. Subsequently, in coordination with the other national teams, the folder and asset structure was defined, following the above mentioned standards.

The migration was divided into two main steps:

* Migration of already generated assets (including vectors, rasters, classifications, ImageCollections, etc.).
* Updating scripts and modules with the new storage paths.

As a final step, functionality testing of the classification processes was conducted to verify correct performance and correct possible errors. This procedure was applied to both the repositories of the general classes (General Map) and those of the transversal methodology.

![Figure 2. New Folder structure and folder levels](https://github.com/vllactayo/mb-cloud-migration/blob/main/gc-workflow.png)

## Support scripts 🫱🏽‍🫲🏽

The MapBiomas Peru team used Python scripts along with the Google Earth Engine API to streamline the asset migration process. These scripts are available in the GitHub repository and enable the following tasks:

* ✅Create multiple folders and/or Image Collections simultaneously.
* ✅Copy a list of assets from one folder to another.
* ✅Delete a group of assets by folder, collection, list, among others.

## Considerations

**Global assets:** Following coordination with the MapBiomas network, the Google Cloud structure will have different repositories to store general inputs such as mosaics, vector layers, etc. Therefore, assets with the following paths have not been migrated:

* *projects/mapbiomas-raisg/MOSAICOS*
* *projects/mapbiomas-raisg/public/*
* *users/mapbiomas/modules*

**Progressive migration:** The migration was carried out in constant communication with the technical team to avoid migrating repositories that are currently in use, thus preventing confusion and script errors.
