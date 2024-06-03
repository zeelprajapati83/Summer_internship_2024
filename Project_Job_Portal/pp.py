import pandas as pd

# Load the Excel file
file_path = 'D:\Program Zeel\project\sheet1.xlsx'
excel_data = pd.read_excel(file_path, sheet_name='Sheet1')  # Replace 'Sheet1' with your sheet name

# Display the first few rows of the DataFrame
print(excel_data.head())

# Extract specific details
# Example: Get all values in a specific column
column_name = 'u_id'
column_data = excel_data[column_name]
print(column_data)

# Example: Filter rows based on a condition
filtered_data = excel_data[excel_data[column_name]== 101]  # Replace 'some_value' with your condition
print(filtered_data)

# Example: Iterate through rows
# for index, row in excel_data.iterrows():
    # print(f"row {index}: {row[column_name]}")

# Save filtered data back to a new Excel file (optional)
# filtered_data.to_excel('filtered_data.xlsx', index=False)
