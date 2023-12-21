import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster

# Load your GeoJSON data
geojson_path = 'bundeslaender.geojson'
gdf = gpd.read_file(geojson_path)

# Remove unnecessary columns
del gdf['BEGINN']
del gdf['WSK']

# Load your CSV data
csv_path = 'fallzahlennachbundesland.csv'  # Replace with the actual file name
data = pd.read_csv(csv_path)

# Merge GeoJSON data with CSV data on the common column
merged_data = gdf.merge(data, left_on='GEN', right_on='Bundesland')

# Convert numeric columns to appropriate types
merged_data['Masernzahlen'] = pd.to_numeric(merged_data['Masernzahlen'], errors='coerce')
merged_data['Impfrate'] = pd.to_numeric(merged_data['Impfrate'], errors='coerce')
merged_data['Per100000'] = pd.to_numeric(merged_data['Per100000'], errors='coerce')

# Create a folium map centered around the mean latitude and longitude of the GeoJSON data
map_center = [merged_data.geometry.centroid.y.mean(), merged_data.geometry.centroid.x.mean()]
m = folium.Map(location=map_center, zoom_start=6)

# Create MarkerClusters for better performance
marker_cluster = MarkerCluster().add_to(m)

# Add GeoJSON layer with measles data
folium.GeoJson(
    merged_data,
    name='Measles Data',
    tooltip=folium.GeoJsonTooltip(fields=['Bundesland', 'Masernzahlen', 'Impfrate', 'Per100000'],
                                  aliases=['Region', 'Measles Cases', 'Vaccination Rate', 'Cases per 100000'],
                                  localize=True),
).add_to(marker_cluster)

# Create Choropleth layer for measles cases per 100000
folium.Choropleth(
    geo_data=merged_data,
    name='Cases per 100000',
    data=merged_data,
    columns=['Bundesland', 'Per100000'],
    key_on='feature.properties.Bundesland',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Cases per 100000',
    highlight=True,
).add_to(m)

# Create Choropleth layer for vaccination rate
folium.Choropleth(
    geo_data=merged_data,
    name='Vaccination Rate',
    data=merged_data,
    columns=['Bundesland', 'Impfrate'],
    key_on='feature.properties.Bundesland',
    fill_color='Purples',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Vaccination Rate',
    highlight=True,
).add_to(m)

# Add additional data as markers
for idx, row in merged_data.iterrows():
    folium.Marker(
        location=[row.geometry.centroid.y, row.geometry.centroid.x],
        popup=f"<strong>{row['Bundesland']}</strong><br>Population: {row['Gesamtbevoelkerung']}<br>Vaccination Rate: {row['Impfrate']}<br>Measles Cases: {row['Masernzahlen']}<br>Cases per 100000: {row['Per100000']:.2f}",
        icon=folium.Icon(color='pink'),
    ).add_to(marker_cluster)

# Add Layer Control to toggle layers
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save('bundeslaender_measles.html')
