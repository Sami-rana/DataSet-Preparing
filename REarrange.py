# import os
# import pandas as pd
#
# # Specify the path to the folder containing CSV files
# folder_path = '/home/sami/PycharmProject/pythonProject1/CSV'
#
# # Get a list of all CSV files in the folder
# csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
#
# # Sort the list of files to ensure a specific order
# csv_files.sort()
#
# # Initialize an empty DataFrame to store the merged data
# merged_data = pd.DataFrame()
#
# # Loop through each CSV file, fill missing values in the "Tag" column, and merge its data into the DataFrame
# for file in csv_files:
#     file_path = os.path.join(folder_path, file)
#     df = pd.read_csv(file_path)
#
#     # Fill missing values in the "Tag" column with "O"
#     df['Tag'].fillna('O', inplace=True)
#
#     merged_data = pd.concat([merged_data, df], ignore_index=True)
#
# # Save the merged DataFrame to a new CSV file
# merged_data.to_csv('//home/sami/PycharmProject/pythonProject1/merged_file.csv', index=False)
#
# print("Merge completed successfully!")
import os
import pandas as pd

# Specify the path to the folder containing CSV files
folder_path = "/home/sami/PycharmProject/pythonProject1/CSV"

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Sort the list of files to ensure a specific order
csv_files.sort()

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Loop through each CSV file, fill missing values in the "Tag" column,
# remove ",O" from the end of values in the "Token" column,
# and merge its data into the DataFrame
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)

    # Fill missing values in the "Tag" column with "O"
    df['Tag'].fillna('O', inplace=True)

    # Remove ",O" from the end of values in the "Token" column
    df['Token'] = df['Token'].str.replace(r',O"', '', regex=True)

    merged_data = pd.concat([merged_data, df], ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_data.to_csv('/home/sami/PycharmProject/pythonProject1/merged_file1.csv', index=False)

print("Merge completed successfully!")
