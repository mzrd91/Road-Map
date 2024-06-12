# Road-Map

# GPS Trajectory Visualization

This project provides a solution for visualizing GPS trajectory data. It includes steps to extract JSON data from Google Maps Timeline, convert it to CSV format, and visualize the data on a map using Python. Additionally, it generates a heatmap and a trajectory map, which can be saved as an image.
The following data is mine, which I requested from Google Takeout. It includes all my destinations and trips within the US so far, even showing my road trip from St. Louis, MO to Temecula, CA. With details, if we could zoom in and zoom out, it shows everything well.

## Step 1: Extract and Convert Data

Extract Location History from Google Takeout, then Convert JSON to CSV [JSON-to-CSV.py](JSON-to-CSV.py)

## Step 2: Visualize Data in both heatmaps.html and Trajedy.html
### Generate Heatmap and Trajectory Map
Use the following script to generate a heatmap and a trajectory map, just run [visualize-data.py](visualize-data.py) 

## How many miles have I gone so far? *Excluding flights*
I have also used the geodesic distance formula [total_miles.py](total_miles.py) to calculate the distance between two GPS points. As a result, the total distance driven is shown as: **"Total distance driven: 41,091.35 miles"** My car's mileage is currently 32,000 miles, which indicates there were times when I traveled without the car.

# Here the results from Heatmaps:

### Southern California:
![heatmaps1](https://github.com/mzrd91/Road-Map/assets/131927177/680eaf2f-3f42-47ba-b0f8-8220fc00449b) 

### The Zoom-Out mode:
![heatmaps 2](https://github.com/mzrd91/Road-Map/assets/131927177/c41c67de-6fab-4471-a279-1fe568bc90ef)

### Overview by video:
https://github.com/mzrd91/Road-Map/assets/131927177/84708eb1-8120-4ee6-8415-4760248f7db3 




