import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from data_preprocessing import preprocess_data
from recommendation_engine import recommend_restaurants
from utils import get_user_preferences

DATA_PATH = "data/Dataset.csv"

def main():
    df = preprocess_data(DATA_PATH)

    cuisine, budget, rating = get_user_preferences()

    recommendations = recommend_restaurants(df, cuisine, budget, rating)

    print("\nRecommended Restaurants:\n")

    if recommendations is None:
        print("No restaurants found matching your preferences.")
    else:
        print(recommendations.to_string(index=False))

if __name__ == "__main__":
    main()
