import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("Smart expense tracker")
st.write("Welcome")

df = pd.read_csv("expense_data.csv")
st.subheader("Your Expenses")
st.dataframe(df)

st.subheader("Spending by Category")
category_total = df.groupby("category")["amount"].sum()

# print(df)
# print(category_total)

st.bar_chart(category_total)

st.subheader("predict Next Month Expense")
#  Drop down menu
category = st.selectbox("Select Category",df["category"].unique())
# filter data for selected category
category_df = df[df["category"] == category]

X = np.array(range(1,len(category_df) + 1)).reshape(-1,1)
y = category_df["amount"].values

# train
model = LinearRegression()
model.fit(X,y)

# predict next month 
next_month = np.array([[len(category_df) + 1]])
prediction = model.predict(next_month)
if prediction[0] < 0:
    st.warning("⚠️ Not enough data to predict accurately!")
else:
    st.success(f"Predicted expense: ₹{prediction[0]:.2f}")

# total spending 
st.header("Monthly Summery")
total = df["amount"].sum()
st.metric("Total Spent",f"₹{total}")