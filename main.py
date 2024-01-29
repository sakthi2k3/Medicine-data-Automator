import pandas as pd

def read_excel_data(file_path, sheet_name='Sheet1'):
    try:
        # Read Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        # Display the data
        print("Excel Data:")
        print(df)
        
        # Return the DataFrame
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
file_path = r'C:\Users\sakth\OneDrive\Desktop\python\Book1.xlsx'  # Replace with the path to your Excel file
sheet_name = 'Sheet1'  # Replace with the sheet name in your Excel file

data_frame = read_excel_data(file_path, sheet_name)
if data_frame is not None:
    # Now you can work with the data_frame as needed
    # For example, you can access specific columns using data_frame['column_name']
    # or iterate through rows using iterrows()

    # Example: Print the values in the 'a' column
    print("\nValues in 'a' column:")
    print(data_frame['a'])
