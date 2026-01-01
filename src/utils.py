def get_user_preferences():
    print("\nEnter your preferences:\n")

    cuisine = input("Preferred Cuisine: ")
    max_budget = float(input("Maximum Budget (Average cost for two): "))
    min_rating = float(input("Minimum Rating: "))

    return cuisine, max_budget, min_rating