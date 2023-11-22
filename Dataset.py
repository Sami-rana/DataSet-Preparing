import os
import pandas as pd

# Specify the path to the folder containing CSV files
folder_path = '/home/sami/PycharmProject/pythonProject1/CSV'

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Sort the list of files to ensure a specific order
csv_files.sort()

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Loop through each CSV file and merge its data into the DataFrame
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    merged_data = pd.concat([merged_data, df], ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_data.to_csv('/home/sami/PycharmProject/pythonProject1/dataset.csv', index=False)

print("Merge completed successfully!")
