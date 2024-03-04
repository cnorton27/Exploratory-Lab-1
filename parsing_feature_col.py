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

    

# Concatenate all GeoDataFrames into a single GeoDataFrame
combined_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True))

# Now combined_gdf contains all the data from all GeoJSON files in the directory,
# and it has a new column 'feature_collection_name' storing the name of each feature collection
print(combined_gdf.head())

# Specify the output GeoJSON file path
output_geojson_file = 'trial.geojson'

# Export GeoDataFrame to GeoJSON
combined_gdf.to_file(output_geojson_file, driver='GeoJSON')

print("GeoDataFrame successfully exported to GeoJSON:", output_geojson_file)



# Read the GeoJSON file into a GeoDataFrame
gdf = gpd.read_file(r'C:\Users\ciara\OneDrive\Documents\GitHub\Exploratory-Lab-1\trial.geojson')

count = 1

# Iterate over every feature in the GeoDataFrame
for index, row in gdf.iterrows():
    count = count + 1
    # Access and modify the value of a specific property using .loc
    gdf.loc[index, 'ID'] = count
    print(gdf.loc[index, 'ID'])

# Save the modified GeoDataFrame to a new GeoJSON file
gdf.to_file('withID.geojson', driver='GeoJSON')
