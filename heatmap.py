import pandas as pd

import geopandas as gpd
import folium

from folium.plugins import MarkerCluster

# Load your GeoJSON data
geojson_path = 'bundeslaender.geojson'
gdf = gpd.read_file(geojson_path)

del gdf['BEGINN']
del gdf['WSK']
csv_path = 'fallzahlennachbundesland.csv'
data = pd.read_csv(csv_path)

# Merge GeoJSON data with CSV data on the common column (replace 'common_column' with your actual common column)
merged_data = gdf.merge(data, left_on='GEN', right_on='Bundesland')

# Create a folium map centered around the mean latitude and longitude of the GeoJSON data
map_center = [merged_data.geometry.centroid.y.mean(), merged_data.geometry.centroid.x.mean()]
m = folium.Map(location=map_center, zoom_start=6)

# Create MarkerClusters for better performance
marker_cluster = MarkerCluster().add_to(m)

# Add GeoJSON layer with measles data
folium.GeoJson(merged_data,
               name='Measles Data',
               tooltip=folium.GeoJsonTooltip(fields=['Bundesland', 'Masernzahlen'],
                                             aliases=['Region', 'Measles Cases'],
                                             localize=True),
               ).add_to(marker_cluster)

# Add additional data as markers
for idx, row in merged_data.iterrows():
    folium.Marker(location=[row.geometry.centroid.y, row.geometry.centroid.x],
                  popup=f"<strong>{row['GEN']}</strong><br>Population: {row['Gesamtbevoelkerung']}<br>Vaccination Rate: {row['Impfrate']}<br>Measles Cases: {row['Masernzahlen']}",
                  icon=folium.Icon(color='blue'),
                  ).add_to(marker_cluster)

# Add Layer Control to toggle layers
folium.LayerControl().add_to(m)

# Add GeoJSON data to the map
folium.GeoJson(merged_data).add_to(m)


# Save the map as an HTML file
m.save('interactive_map.html')
