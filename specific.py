import pandas as pd
def get_column_from_excel(excel_path, column_name):
    try:
        # Read Excel sheet into a DataFrame
        df = pd.read_excel(excel_path)

        # Check if the specified column exists in the DataFrame
        if column_name in df.columns:
            # Extract the specified column as a list
            column_values = df[column_name].tolist()
            return column_values
        else:
            print(f"Error: Column '{column_name}' not found in the Excel sheet.")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
excel_file_path = 'meds.xlsx'  # Replace with the path to your Excel file
column_name_to_extract = 'name'  # Replace with the name of the column you want to extract


result = get_column_from_excel(excel_file_path, column_name_to_extract)

# if result is not None:
#     print(f"Values in '{column_name_to_extract}':")
#     print(result)
      