import geopandas as gpd
import pandas as pd
import numpy as np
import requests
import os
import glob

# Directory containing GeoJSON files
directory = r'C:\Users\ciara\OneDrive\Documents\GitHub\Exploratory-Lab-1\Squamish_Nation_plants'

# Get a list of all GeoJSON files in the directory
geojson_files = glob.glob(os.path.join(directory, '*.geojson'))

# Create an empty list to store GeoDataFrames
gdfs = []

# Iterate over each GeoJSON file and load it into GeoDataFrame
for file in geojson_files:
    # Read GeoJSON file
    feature_collection_name = os.path.splitext(os.path.basename(file))[0]
    gdf = gpd.read_file(file)

    gdf['feature_collection_name'] = feature_collection_name
    print(feature_collection_name)
    

    # Append GeoDataFrame to list
    gdfs.append(gdf)

# Concatenate all GeoDataFrames into a single GeoDataFrame
combined_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True))

# Now combined_gdf contains all the data from all GeoJSON files in the directory,
# and it has a new column 'feature_collection_name' storing the name of each feature collection
print(combined_gdf.head())

# Specify the output GeoJSON file path
output_geojson_file = 'output_noroads.geojson'

# Export GeoDataFrame to GeoJSON
combined_gdf.to_file(output_geojson_file, driver='GeoJSON')

print("GeoDataFrame successfully exported to GeoJSON:", output_geojson_file)