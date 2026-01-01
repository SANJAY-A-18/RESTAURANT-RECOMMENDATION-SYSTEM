import pandas as pd

def preprocess_data(file_path):
    print("Loading and preprocessing data...")

    df = pd.read_csv(file_path)

    # Select only required columns
    required_columns = [
        "Restaurant Name",
        "Cuisines",
        "Average Cost for two",
        "Aggregate rating",
        "City"
    ]
    df = df[required_columns]

    # Handle missing values
    df["Cuisines"] = df["Cuisines"].fillna("Unknown")
    df["Average Cost for two"] = df["Average Cost for two"].fillna(
        df["Average Cost for two"].median()
    )
    df["Aggregate rating"] = df["Aggregate rating"].fillna(
        df["Aggregate rating"].median()
    )

    return df
