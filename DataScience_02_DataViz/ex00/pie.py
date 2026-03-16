import pandas as pd
import os
from pathlib import Path


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def load_customers() -> pd.DataFrame:
    dfs = []
    script_dir = Path(__file__).parent
    data_path = (script_dir / "../subject/customer").resolve()
    path = "DataScience_02_DataViz/subject/customer/"

    if not data_path.exists():
        print(f"{data_path} Folder not found!")
        return

    for file in data_path.glob("*.csv"):
        table_path = path + file.stem + ".csv"
        dfs.append(load_data(table_path))
    contacts = pd.concat(dfs)
    contacts['event_time'] = pd.to_datetime(contacts['event_time'])
    return (contacts)


def load_items():
    df = load_data("DataScience_02_DataViz/subject/item/item.csv")
    return df


def merge_data(items, customers) -> pd.DataFrame:
    df = pd.merge(customers, items, on="product_id")
    return df


def remove_doubles(df: pd.DataFrame):

    df = df.sort_values(by=['product_id', 'event_type', 'event_time'])
    time_diff = df.groupby(['product_id', 'event_type'])['event_time'].diff()
    df_cleaned = df[~(time_diff <= pd.Timedelta(seconds=1))]
    return df_cleaned


# def main():
if __name__ == "__main__":
    customers = load_customers()
    customers = remove_doubles(customers)
    items = load_items()
    customers = merge_data(items, customers)
    print(customers.describe())
