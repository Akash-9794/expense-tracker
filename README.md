# 💰 Smart Expense Tracker with AI Insights

A web app that automatically categorizes your expenses using AI and predicts your next month's spending using Machine Learning.

🔗 **Live Demo:** [Your Streamlit App Link Here]

---

## 📌 What It Does

- 📂 Loads your expense data from a CSV file
- 🤖 Auto-categorizes expenses using keyword-based AI (Food, Transport, Shopping, etc.)
- 📊 Shows a visual bar chart of spending by category
- 🔮 Predicts next month's expense for any category using Linear Regression
- 💡 Displays total spending summary

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Data Handling | Pandas, NumPy |
| ML Model | Scikit-learn (Linear Regression) |
| Web Dashboard | Streamlit |
| Storage | CSV |
| Deployment | Streamlit Cloud |

---

## 📁 Project Structure

```
expense-tracker/
│
├── app.py                # Main Streamlit app
├── expense_data.csv      # Expense dataset
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## 🚀 How to Run Locally

**1. Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/expense-tracker.git
cd expense-tracker
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the app:**
```bash
streamlit run app.py
```

---

## 🧠 How AI Works Here

The app uses **keyword matching** to auto-categorize expenses:

```
"morning coffee"     → Food
"auto to college"    → Transport
"pharmacy medicine"  → Healthcare
```

The **ML model (Linear Regression)** learns from past monthly expenses and predicts future spending for each category.

---

## 📸 Screenshots

> Add screenshots of your app here

---

## 👨‍💻 Built By

**Akash Chaurasiya**
- GitHub: [@akashchaurasiy6](https://github.com/akashchaurasiy6)
- LinkedIn: [Your LinkedIn Link]

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
