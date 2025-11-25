import pandas as pd

# ====================================================
# Class 1: Load Data
# ====================================================
class DataLoader:
    """
    DataLoader class handles loading CSV data.
    """

    def __init__(self, file_path: str):
        self._file_path = file_path
        self._data = None

    def load_csv(self, encoding: str = "latin1") -> pd.DataFrame:
        """
        Load CSV file into a pandas DataFrame.
        """
        self._data = pd.read_csv(self._file_path, encoding=encoding)
        return self._data


# ====================================================
# Class 2: Data Processing
# ====================================================
class Processing(DataLoader):
    """
    Processing class handles cleaning and preprocessing of data.
    Inherits DataLoader.
    """

    def clean_data(self) -> pd.DataFrame:
        """
        Clean price, odometer, and filter invalid data.
        """
        # Clean price column
        self._data['price'] = (
            self._data['price']
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .astype(float)
        )

        # Clean odometer column
        self._data['odometer'] = (
            self._data['odometer']
            .str.replace("km", "", regex=False)
            .str.replace(",", "", regex=False)
            .astype(float)
        )

        # Remove invalid year + price
        self._data = self._data[
            (self._data['yearOfRegistration'] >= 1900) &
            (self._data['yearOfRegistration'] <= 2020)
        ]

        self._data = self._data[
            (self._data['price'] >= 500) &
            (self._data['price'] <= 500000)
        ]

        return self._data


# ====================================================
# Class 3: Analysis
# ====================================================
class Analysis(Processing):
    """
    Analysis class performs statistical summaries and aggregations.
    Inherits Processing.
    """

    def brand_price_stats(self) -> dict:
        """
        Compute highest, lowest, and widest range of prices by brand.
        """

        brand_price = self._data.groupby("brand")["price"]
        sorted_mean = brand_price.mean().sort_values(ascending=False)

        highest = f"{sorted_mean.index[0]} has the highest average price"
        lowest = f"{sorted_mean.index[-1]} has the lowest average price"

        widest_range = (
            brand_price.agg(lambda x: x.max() - x.min())
            .sort_values(ascending=False)
            .index[0]
        )

        return {
            "highest_avg_brand": highest,
            "lowest_avg_brand": lowest,
            "widest_range_brand": f"{widest_range} has the widest price range"
        }

    def yearly_brand_analysis(self, top_n: int = 5) -> dict:
        """
        Compute top brands by average price per year.
        """

        yearly_avg = (
            self._data.groupby(["yearOfRegistration", "brand"])["price"]
            .mean()
            .sort_values(ascending=False)
        )

        top_year, top_brand = yearly_avg.index[0]
        top_value = yearly_avg.iloc[0]

        highest_year_brand = (
            f"In {top_year}, {top_brand} had the highest average price: {top_value}"
        )

        return {
            "highest_year_brand": highest_year_brand,
            "top_n_year_brand": yearly_avg.head(top_n)
        }

    def run_analysis(self) -> dict:
        """
        Execute all analysis.
        """
        results = {}
        results.update(self.brand_price_stats())
        results.update(self.yearly_brand_analysis())
        return results

    def export_cleaned_data(self, file_name: str = "auto_cleaned.csv"):
        """
        Export cleaned data.
        """
        self._data.to_csv(file_name, index=False)
        print(f"Cleaned data exported to {file_name}")

    def export_analysis_results(self, results: dict, file_name: str = "auto_analysis.csv"):
        """
        Export analysis results to CSV.
        """
        export_dict = {}

        for key, value in results.items():
            if isinstance(value, (pd.Series, pd.DataFrame)):
                export_dict[key] = value.to_string()
            else:
                export_dict[key] = value

        pd.DataFrame([export_dict]).to_csv(file_name, index=False)
        print(f"Analysis results exported to {file_name}")


# ====================================================
# Example usage
# ====================================================
if __name__ == "__main__":

    file_path = "autos.csv"

    analyzer = Analysis(file_path)
    analyzer.load_csv()
    analyzer.clean_data()

    results = analyzer.run_analysis()

    analyzer.export_cleaned_data()
    analyzer.export_analysis_results(results)

    # Show results in terminal
    for key, value in results.items():
        print(f"\n{key}:\n{value}")