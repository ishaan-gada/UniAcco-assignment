import argparse
import csv
import pandas as pd

def load_csv_file(filename):
    try:
        with open(filename, "r") as file:
            data = list(csv.reader(file))
            return data
    except FileNotFoundError:
        print(f"Error: file {filename} not found")
        return None

def count_rows(data):
    print(f"Number of rows: {len(data)-1}")

def calculate_mean(data, column):
    column_index = data[0].index(column)
    values = [float(row[column_index]) for row in data[1:]]
    mean = sum(values) / len(values)
    print(f"Mean of column {column}: {mean}")

def filter_data(data, column, value):
    column_index = data[0].index(column)
    filtered_data = [data[0]]
    for row in data[1:]:
        if row[column_index] == value:
            filtered_data.append(row)
    print(f"Filtered data: {filtered_data}")

def sort_data(data, column):
    sorted_data = sorted(data[1:], key=lambda row: row[data[0].index(column)])
    sorted_data.insert(0, data[0])
    print(f"Sorted data: {sorted_data}")

def calculate_std(data, column):
    values = [float(row[data[0].index(column)]) for row in data[1:]]
    std = pd.Series(values).std()
    print(f"Standard deviation of column {column}: {std}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process CSV files")
    parser.add_argument("filename", help="CSV filename to process")
    args = parser.parse_args()

    data = load_csv_file(args.filename)
    if data is None:
        exit()

    while True:
        command = input("Enter command: ")
        if command == "exit":
            break
        elif command == "help":
            print("Available commands:")
            print("- load <filename>: Load a CSV file into memory.")
            print("- count: Count the number of rows in the currently loaded CSV file.")
            print("- mean <column>: Calculate the mean of a numeric column in the currently loaded CSV file.")
            print("- filter <column> <value>: Filter the currently loaded CSV file to include only rows where the specified column matches the specified value.")
            print("- sort <column>: Sort the currently loaded CSV file by the specified column.")
            print("- std <column>: Calculate the standard deviation of a numeric column in the currently loaded CSV file.")
            print("- help: Show available commands.")
            print("- exit: Exit the program.")
        else:
            parts = command.split()
            if len(parts) == 0:
                continue

            if parts[0] == "load":
                if len(parts) != 2:
                    print("Error: load command requires a filename argument")
                else:
                    data = load_csv_file(parts[1])
            elif parts[0] == "count":
                count_rows(data)
            elif parts[0] == "mean":
                if len(parts) != 2:
                    print("Error: mean command requires a column argument")
                else:
                    calculate_mean(data, parts[1])
            elif parts[0] == "filter":
                if len(parts) != 3:
                    print("Error: filter command requires a column and value argument")
                else:
                    filter_data(data, parts[1], parts[2])
            elif parts[0] == "sort":
                if len(parts) != 2:
                    print("Error: sort command requires a column argument")
                else:
                    sort_data(data, parts[1])
            elif parts[0] == "std":
                if len(parts) != 2:
                    print("Error: std command requires a column argument")
                else:
                    calculate_std(data, parts[1])
            else:
                print(f"Error: unknown command '{parts[0]}'")
                exit()
                
                    
                
            




