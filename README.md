Auto Data Processing Project

This project provides an object-oriented Python pipeline to load, clean, and analyze automobile data using Pandas. It includes two main classes: DataLoader and Processing. The project handles data cleaning, filtering, and basic statistical analysis on the dataset.

Project Structure

DataLoader: Loads CSV data.

Processing: Inherits DataLoader and performs data cleaning and analysis.

How It Works
DataLoader

Responsible for reading CSV files.

load_csv(): Loads the CSV file using pandas and stores it in the class.

Processing (inherits DataLoader)

Cleans the dataset and performs analysis.
Cleaning steps include:

Removing "$" and commas from price.

Removing "km" and commas from odometer.

Converting values to integers.

Filtering invalid registration years (1900–2020).

Filtering unrealistic price values (500–500000).

Analysis Functions

highest_avg_price(): Prints the brand with the highest average price.

least_avg_price(): Prints the brand with the lowest average price.

widest_range(): Prints the brand with the widest price range (max - min).

highest_avg_price_by_year(): Shows which brand and year combination has the highest average price.

Usage Example

processor = Processing("data.csv")
auto = processor.load_csv()
auto = processor.data_cleaning()

processor.highest_avg_price()
processor.least_avg_price()
processor.widest_range()
processor.highest_avg_price_by_year()

Requirements
Python 3.x
pandas

Install pandas:
pip install pandas
