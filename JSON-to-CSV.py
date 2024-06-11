import json
import csv

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

print("Data has been successfully written to Records.csv")
