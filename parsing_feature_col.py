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
    ID= 0
    
    gdf = gpd.read_file(file)
    gdf["ID"] = ID
    gdf['feature_collection_name'] = feature_collection_name
    print(feature_collection_name)

    # Append GeoDataFrame to list
    gdfs.append(gdf)

    
combined_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True))


print(combined_gdf.head())

output_geojson_file = 'trial.geojson'

# Export to JSON
combined_gdf.to_file(output_geojson_file, driver='GeoJSON')

# Read the GeoJSON file into a GeoDataFrame
gdf = gpd.read_file(r'C:\Users\ciara\OneDrive\Documents\GitHub\Exploratory-Lab-1\trial.geojson')

count = 1

# Adding ID column using count
for index, row in gdf.iterrows():
    count = count + 1
    # Access and modify the value new ID property using .loc
    gdf.loc[index, 'ID'] = count
    print(gdf.loc[index, 'ID'])

# Save as a new GeoJSON file
gdf.to_file('withID.geojson', driver='GeoJSON')
