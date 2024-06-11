import json
import csv

# Load JSON data
with open('Records.json', 'r') as json_file:
    data = json.load(json_file)
# Extract relevant data
locations = data['locations']
# Write to CSV
with open('Records.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write headers
    csv_writer.writerow(['timestampMs', 'latitudeE7', 'longitudeE7', 'accuracy'])

    for location in locations:
        if all(key in location for key in ['timestampMs', 'latitudeE7', 'longitudeE7', 'accuracy']): 
            csv_writer.writerow([location['timestampMs'], location['latitudeE7'], location['longitudeE7'], location['accuracy']])
        else:
            print(f"Skipping location due to missing keys: {location}") # Print locations that are skipped
