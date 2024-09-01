import argparse
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Decorator for logging function execution
def log_execution(func):
    def wrapper(*args, **kwargs):
        logging.info(f'Executing {func.__name__} with arguments: {args}, {kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'Execution of {func.__name__} completed.')
        return result
    return wrapper

# Generator for processing data rows
def filter_rows(dataframe, column, value):
    for _, row in dataframe.iterrows():
        if row[column] == value:
            yield row

# Function to process the file
@log_execution
def process_file(input_file, output_file, column, value, print_to_console):
    # Read the CSV file
    df = pd.read_csv(input_file)
    logging.info(f'Loaded file: {input_file}')
    
    # Filter data
    filtered_data = list(filter_rows(df, column, value))
    logging.info(f'Filtered data based on column "{column}" and value "{value}"')
    
    # Output the result
    if print_to_console:
        for row in filtered_data:
            print(row.to_dict())
    else:
        filtered_df = pd.DataFrame(filtered_data)
        filtered_df.to_csv(output_file, index=False)
        logging.info(f'Saved filtered data to: {output_file}')

# CLI Setup
def main():
    parser = argparse.ArgumentParser(description='Process a CSV file and filter data based on column values.')
    
    parser.add_argument('input_file', type=str, help='Path to the input CSV file')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file')
    parser.add_argument('column', type=str, help='Column name to filter on')
    parser.add_argument('value', type=str, help='Value to filter on')
    parser.add_argument('-p', '--print', action='store_true', help='Print results to console instead of saving to file')
    
    args = parser.parse_args()
    
    process_file(args.input_file, args.output_file, args.column, args.value, args.print)

if __name__ == '__main__':
    main()
