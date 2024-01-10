import pandas as pd

def convert_xlsx_to_csv(input_path, output_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(input_path)

    # Write the DataFrame to a CSV file
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # Replace 'input_file.xlsx' with the name of your Excel file
    input_file = 'mementos_count.xlsx'

    # Replace 'output_file.csv' with the desired name for the CSV file
    output_file = 'mementos_count.csv'

    convert_xlsx_to_csv(input_file, output_file)
    print(f"Conversion completed. CSV file saved as '{output_file}'.")
