import json
import csv
import pandas as pd
import folium
from folium.plugins import HeatMap

# Load JSON data
try:
    with open('Records.json', 'r') as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print("The JSON file was not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error decoding JSON.")
    exit(1)

if 'locations' not in data:
    print("'locations' key not found in JSON data.")
    exit(1)

locations = data['locations']

# Write to CSV
try:
    with open('Records.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['timestamp', 'latitudeE7', 'longitudeE7', 'accuracy'])

        # Write data rows
        row_count = 0
        for location in locations:
            # Use 'timestamp' instead of 'timestampMs'
            if all(key in location for key in ['timestamp', 'latitudeE7', 'longitudeE7', 'accuracy']): 
                csv_writer.writerow([location['timestamp'], location['latitudeE7'], location['longitudeE7'], location['accuracy']])
                row_count += 1
            else:
                print(f"Skipping location due to missing keys: {location}") # Print locations that are skipped

        print(f"Total rows written: {row_count}")

except IOError:
    print("Error writing to CSV file.")
    exit(1)

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

# Convert latitude and longitude from E7 format to standard format
data['latitude'] = data['latitudeE7'] / 1e7
data['longitude'] = data['longitudeE7'] / 1e7

# Function to calculate total distance using geopy
def calculate_total_distance(df):
    total_distance = 0.0
    for i in range(1, len(df)):
        start_coords = (df.iloc[i-1]['latitude'], df.iloc[i-1]['longitude'])
        end_coords = (df.iloc[i]['latitude'], df.iloc[i]['longitude'])
        total_distance += geodesic(start_coords, end_coords).miles
    return total_distance

# Calculate total distance driven
total_distance = calculate_total_distance(data)
print(f"Total distance driven: {total_distance:.2f} miles")


