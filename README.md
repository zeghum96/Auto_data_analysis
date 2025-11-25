# 🚗 Auto Data Processing & Analysis

A complete **object-oriented Python project** for loading, cleaning, and analyzing automobile datasets using **Pandas**.  
This project demonstrates practical **OOP design**: `DataLoader → Processing → Analysis`.

---

## Features

### Data Loading
- Reads CSV files using Pandas
- Supports custom encoding

### Data Cleaning
- Removes symbols (`$`, `km`, `,`)
- Converts price and odometer to integers
- Filters invalid years (1900–2020)
- Filters unrealistic prices (500–500,000)
- Resets index for a clean DataFrame

### Data Analysis
- Brand with the **highest average price**
- Brand with the **lowest average price**
- Brand with the **widest price range**
- Highest average price by **year + brand**
- Export results to CSV

---

## Project Architecture


### DataLoader
- Handles reading CSV data
- Stores data in class instance

### Processing (inherits DataLoader)
- Performs data cleaning
- Applies filtering
- Returns cleaned DataFrame

### Analysis (inherits Processing)
- Performs brand-wise & year-wise analysis
- Returns results as dictionary
- Exports results to CSV

---

## Example Usage

```python
process = Analysis("autos.csv")
process.load_csv()
process.clean_data()

results = process.run_analysis()

process.export_cleaned_data()
process.export_analysis_results(results)

for key, value in results.items():
    print(f"{key}:\n{value}\n")
## Output Example

- BMW has the highest average price
- Renault has the lowest average price
- Audi has the widest price range
- In 2016, brand Porsche had the highest average price

---

## File Export

- `auto_cleaned.csv` → Cleaned Dataset
- `auto_analysis.csv` → Analysis Summary

---

## Requirements

- Python 3.8+
- pandas

Install dependencies:

```bash
pip install pandas
