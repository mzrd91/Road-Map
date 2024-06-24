import pandas as pd
import folium
from folium.plugins import HeatMap

# Load the CSV data
csv_file_path = 'Records.csv'
data = pd.read_csv(csv_file_path)

# Convert latitude and longitude from E7 format to standard format
data['latitude'] = data['latitudeE7'] / 1e7
data['longitude'] = data['longitudeE7'] / 1e7

# Display the first few rows of the dataframe to ensure it's loaded correctly
print(data.head())

# Initialize a map centered around the mean coordinates for the heatmap
map_center = [data['latitude'].mean(), data['longitude'].mean()]
heatmap = folium.Map(location=map_center, zoom_start=10)

# Prepare data for the heatmap
heat_data = data[['latitude', 'longitude']].values.tolist()

# Create and add the heatmap to the map
HeatMap(heat_data).add_to(heatmap)

# Save the heatmap to an HTML file
heatmap.save('heatmap.html')
print("Heatmap has been created and saved to heatmap.html")

# Initialize a map centered around the mean coordinates for the trajectory map
trajectory_map = folium.Map(location=map_center, zoom_start=10)

# Add lines connecting the GPS points
folium.PolyLine(data[['latitude', 'longitude']].values, color='blue', weight=2.5, opacity=1).add_to(trajectory_map)

# Optionally, add markers for each point
for index, row in data.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=f"Timestamp: {row['timestamp']}").add_to(trajectory_map)

# Save the trajectory map to an HTML file
trajectory_map.save('trajectory_map.html')
print("Trajectory map has been created and saved to trajectory_map.html")
