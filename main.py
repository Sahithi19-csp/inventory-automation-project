import argparse
from src.extract import load_inventory
from src.process import clean_data
from src.update import save_cleaned_data
from src.alert import flag_low_stock

def run(input_path, output_path):
    df = load_inventory(input_path)
    df = clean_data(df)
    low_stock_df = flag_low_stock(df)
    save_cleaned_data(df, output_path)
    print(f"Low stock items:\n{low_stock_df[['SKU', 'ReorderQty']]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/inventory_raw.csv")
    parser.add_argument("--output", default="data/inventory_cleaned.csv")
    args = parser.parse_args()
    run(args.input, args.output)
