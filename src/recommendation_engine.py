def recommend_restaurants(df, cuisine, max_budget, min_rating):
    cuisine = cuisine.lower()

    filtered_df = df[
        (df["Cuisines"].str.lower().str.contains(cuisine)) &
        (df["Average Cost for two"] <= max_budget) &
        (df["Aggregate rating"] >= min_rating)
    ]

    if filtered_df.empty:
        return None

    return filtered_df.sort_values(
        by="Aggregate rating",
        ascending=False
    ).head(5)