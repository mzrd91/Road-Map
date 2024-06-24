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
