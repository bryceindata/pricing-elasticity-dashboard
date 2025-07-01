import pandas as pd

def load_data(path="data/sample_sku_sales.csv"):
    df = pd.read_csv(path, parse_dates=["Date"])
    return df
