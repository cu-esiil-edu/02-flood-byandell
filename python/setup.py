"""Setup script for the Cheyenne River flood analysis.

This script mirrors the initial setup code from notebooks/flood-00-setup.ipynb.

What it does:
1. Imports the libraries needed to work with tabular and spatial data.
2. Defines key workflow variables, such as the site name and project title.
3. Creates a project folder and downloads the sample flood data using earthpy.
4. Prints the download location and lists the files to verify the download.
"""

import os
import earthpy
import geopandas as gpd
import pandas as pd
import plotly.express as px

# Important workflow variables
id = "stars"
site_name = "Cheyenne River near Wasta"
year = 2019
project_title = "Cheyenne River Flood Frequency"
project_dirname = "flood-cheyenne"

# Create the project directory and download sample data
project = earthpy.Project(title=project_title, dirname="flood-cheyenne-data")
data_dir = project.get_data()

# Display the project data directory location
print("Project directory:", project.project_dir)
print("Downloaded data directory:", data_dir)

# List the contents of the project directory to verify the download
print("\nDirectory contents:")
for item in sorted(os.listdir(project.project_dir)):
    print("-", item)

# Wrap-up note
print("\nSetup complete. Use the variables defined here in other scripts or notebooks.")
