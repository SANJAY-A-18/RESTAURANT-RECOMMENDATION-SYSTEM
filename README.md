# 🍽️ Restaurant Recommendation System

This project implements a **content-based restaurant recommendation system** that suggests restaurants based on user preferences.

---

## 🎯 Objective
The goal of this project is to recommend restaurants by considering:
- Preferred cuisine
- Budget constraints
- Minimum rating requirement

This helps users quickly discover restaurants that match their tastes and affordability.

---

## 🧠 Approach
- Load and preprocess the restaurant dataset
- Apply content-based filtering techniques
- Filter restaurants based on user inputs
- Rank recommendations by rating
- Display the top recommended restaurants

---

## 📂 Project Structure

```
Restaurant_Recommendation_System/
│
├── data/
│   └── Dataset.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── recommendation_engine.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

---

## 📌 Sample Input

```
Preferred Cuisine: North Indian
Maximum Budget: 500
Minimum Rating: 4
```

---

## 📊 Output
The system displays the **top recommended restaurants** that best match the user’s preferences, sorted by rating.

---

## 🚀 Key Features
- Simple and intuitive recommendation logic  
- Content-based filtering approach  
- Modular and readable code structure  
- Easy to extend with additional filters or ML models  

---

## 🔮 Future Enhancements
- Add collaborative filtering  
- Include location-based recommendations  
- Deploy as a web application  
- Improve ranking using machine learning models  

---

## 🏁 Author
**Sanjay**