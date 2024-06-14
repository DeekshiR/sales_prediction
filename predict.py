# import streamlit as st
# import numpy as np
# from datetime import datetime, timedelta
# import pickle
# import random
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the model
# model = pickle.load(open("model.pkl", "rb"))


# def preprocessdata(
#     Store,
#     Dept,
#     Date,
#     Temperature,
#     Fuel_Price,
#     Type_B,
#     Type_C,
#     IsHoliday_True,
#     Unemployment,
# ):
#     # Convert inputs to the correct types
#     Store = int(Store)
#     Dept = int(Dept)
#     Date = datetime.strptime(Date, "%Y-%m-%d")
#     month_date = Date.month
#     day_date = Date.day
#     year_date = Date.year
#     Temperature = float(Temperature)
#     Fuel_Price = float(Fuel_Price)
#     Type_B = bool(Type_B)
#     Type_C = bool(Type_C)
#     IsHoliday_True = bool(IsHoliday_True)
#     # Assume random values for the missing features
#     MarkDown1 = random.uniform(2000, 10000)
#     MarkDown2 = random.uniform(2000, 10000)
#     MarkDown3 = random.uniform(2000, 10000)
#     MarkDown4 = random.uniform(2000, 10000)
#     MarkDown5 = random.uniform(2000, 10000)
#     CPI = 171.578434
#     Size = random.uniform(500, 1000)

#     # Create the test data list
#     test_data = [
#         [
#             Store,
#             Dept,
#             Temperature,
#             Fuel_Price,
#             MarkDown1,
#             MarkDown2,
#             MarkDown3,
#             MarkDown4,
#             MarkDown5,
#             CPI,
#             Unemployment,
#             Size,
#             month_date,
#             day_date,
#             year_date,
#             Type_B,
#             Type_C,
#             IsHoliday_True,
#         ]
#     ]

#     # Make a prediction
#     prediction = model.predict(test_data)

#     # Format the prediction output
#     output = prediction[0]

#     return output


# def predict_sales_for_month(
#     start_date,
#     Store,
#     Dept,
#     Temperature,
#     Fuel_Price,
#     Type_B,
#     Type_C,
#     IsHoliday_True,
#     Unemployment,
# ):
#     predictions = []
#     current_date = start_date
#     while current_date.month == start_date.month:
#         prediction = preprocessdata(
#             Store,
#             Dept,
#             str(current_date),
#             Temperature,
#             Fuel_Price,
#             Type_B,
#             Type_C,
#             IsHoliday_True,
#             Unemployment,
#         )
#         predictions.append(prediction)
#         current_date += timedelta(days=1)
#     return predictions


# def main():
#     st.title("Sales Prediction")

#     st.sidebar.header("Input Parameters")

#     start_date = st.sidebar.date_input("Start Date")
#     Store = st.sidebar.number_input("Store", min_value=1, max_value=45, step=1)
#     Dept = st.sidebar.number_input("Dept", min_value=1, max_value=99, step=1)
#     Temperature = st.sidebar.number_input("Temperature", value=0.0)
#     Fuel_Price = st.sidebar.number_input("Fuel Price", value=0.0)
#     Type_B = st.sidebar.checkbox("Type B")
#     Type_C = st.sidebar.checkbox("Type C")
#     IsHoliday_True = st.sidebar.checkbox("Is Holiday")
#     Unemployment = st.sidebar.number_input("Unemployment", value=0.0)

#     if st.sidebar.button("Predict"):
#         predictions = predict_sales_for_month(
#             start_date,
#             Store,
#             Dept,
#             Temperature,
#             Fuel_Price,
#             Type_B,
#             Type_C,
#             IsHoliday_True,
#             Unemployment,
#         )

#         # Create a DataFrame with dates and predicted sales
#         dates = pd.date_range(start=start_date, periods=len(predictions), freq="D")
#         df = pd.DataFrame({"Date": dates, "Predicted Sales": predictions})

#         # Plot the predictions
#         plt.figure(figsize=(10, 6))
#         plt.plot(df["Date"], df["Predicted Sales"], marker="o", linestyle="-")
#         plt.xlabel("Date")
#         plt.ylabel("Predicted Sales")
#         plt.title("Predicted Sales for One Month")
#         plt.xticks(rotation=45)
#         st.pyplot(plt)


# if __name__ == "__main__":
#     main()

import streamlit as st
import numpy as np
from datetime import datetime
import pickle
import random

# Load the model
model = pickle.load(open("model.pkl", "rb"))


def preprocessdata(
    Store,
    Dept,
    Date,
    Temperature,
    Fuel_Price,
    Type_B,
    Type_C,
    IsHoliday_True,
    Unemployment,
):
    # Convert inputs to the correct types
    Store = int(Store)
    Dept = int(Dept)
    Date = datetime.strptime(Date, "%Y-%m-%d")
    month_date = Date.month
    day_date = Date.day
    year_date = Date.year
    Temperature = float(Temperature)
    Fuel_Price = float(Fuel_Price)
    Type_B = bool(Type_B)
    Type_C = bool(Type_C)
    IsHoliday_True = bool(IsHoliday_True)
    # Assume random values for the missing features
    MarkDown1 = random.uniform(0, 1000)
    MarkDown2 = random.uniform(0, 1000)
    MarkDown3 = random.uniform(0, 1000)
    MarkDown4 = random.uniform(0, 1000)
    MarkDown5 = random.uniform(0, 1000)
    CPI = random.uniform(100, 300)
    Size = random.uniform(10000, 200000)

    # Create the test data list
    test_data = [
        [
            Store,
            Dept,
            Temperature,
            Fuel_Price,
            MarkDown1,
            MarkDown2,
            MarkDown3,
            MarkDown4,
            MarkDown5,
            CPI,
            Unemployment,
            Size,
            month_date,
            day_date,
            year_date,
            Type_B,
            Type_C,
            IsHoliday_True,
        ]
    ]

    # Make a prediction
    prediction = model.predict(test_data)

    # Format the prediction output
    output = prediction[0]

    return output


def main():
    st.title("Sales Prediction")

    st.header("Input Parameters")

    Store = st.number_input("Store Id", min_value=1, max_value=45, step=1)
    Dept = st.number_input("Dept Id", min_value=1, max_value=99, step=1)
    Date = st.date_input("Date")
    Temperature = st.number_input("Temperature", value=0.0)
    Fuel_Price = st.number_input("Fuel Price", value=0.0)
    Type_B = st.checkbox("Type B")
    Type_C = st.checkbox("Type C")
    IsHoliday_True = st.checkbox("Is Holiday")
    Unemployment = st.number_input("Unemployment", value=0.0)

    if st.button("Predict"):
        prediction = preprocessdata(
            Store,
            Dept,
            str(Date),
            Temperature,
            Fuel_Price,
            Type_B,
            Type_C,
            IsHoliday_True,
            Unemployment,
        )
        st.write(f"<h2>Predicted Sales: $ {prediction}</h2>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
