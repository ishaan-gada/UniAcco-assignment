# UniAcco-assignment
 Code for  a Command line tool to read and perform opeations on csv files 
 CSV Tool
CSV Tool is a command-line tool for working with CSV files. It can load a CSV file into memory, perform various operations on the data, and save the modified data back to a CSV file.
Requirements
Python 3.x
argparse
pandas
csv


Loading a CSV file
To load a CSV file, simply run the script with the path to the CSV file as the only argument:
Example-
$ python csv_tool.py example.csv(filename)


Displaying help
To display a list of available command-line options, use the help option:
enter a command : help


Counting the number of rows
To count the number of rows in the loaded CSV file, use the --count option:
enter a command : count
output -There are 4 rows in the loaded CSV file


Sorting the data
To sort the data by a column, use the --sort option followed by the name of the column to sort by:
enter a command : sort name(row name to sort with) 
output : Sorted data by name column


Calculating the mean of a numeric column
To calculate the mean of a numeric column, use the --mean option followed by the name of the numeric column:
enter a command : mean age
output:Mean of age column: 32.0


Calculating the standard deviation of a numeric column
To calculate the standard deviation of a numeric column, use the --std option followed by the name of the numeric column:
enter a command :std age
Output: Standard deviation of age column: 7.9372


Filtering the data
To filter the data to include only rows where a column matches a certain value, use the --filter option followed by the name of the column and the desired value:
enter a command :filter gender female 
output: Filtered data to include only rows where gender = female

