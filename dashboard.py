import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objects as go
import matplotlib
import seaborn as sns
import pickle
import matplotlib.pyplot as plt

# Load data
with open("train_with_feature_final.pkl", "rb") as file:
    train_data = pickle.load(file)


# def main():
#     st.title("Dashboard")

#     st.write("What is the average weekly sales month-wise?")
#     avg_sales_by_month = (
#         train_data.groupby("Month")["Weekly_Sales"].mean().reset_index()
#     )
#     fig1 = px.bar(
#         avg_sales_by_month,
#         x="Month",
#         y="Weekly_Sales",
#         title="Average Weekly Sales by Month",
#     )
#     st.plotly_chart(fig1)

#     st.write("Average Weekly Sales by Department")
#     avg_sales_by_store = (
#         train_data.sample(1000).groupby(["Dept"])["Weekly_Sales"].mean().reset_index()
#     )
#     fig = px.bar(
#         avg_sales_by_store,
#         x="Dept",
#         y="Weekly_Sales",
#         title="Average Weekly Sales by Department",
#     )
#     fig.update_layout(
#         xaxis_title="Department",
#         yaxis_title="Average Weekly Sales",
#         xaxis_tickangle=-45,
#     )
#     st.plotly_chart(fig)

#     # fig3 = px.line(
#     #     avg_sales_by_month,
#     #     x="Day",
#     #     y="Weekly_Sales",
#     #     color="Month",
#     #     title="Average Weekly Sales by Day",
#     #     labels={"Day": "Day", "Weekly_Sales": "Average Weekly Sales"},
#     # )

#     # st.plotly_chart(fig3)
#     # st.write("Weekly Sales vs. Week of Year")
#     # fig3, ax = matplotlib.pyplot.subplots(figsize=(10, 6))
#     # sns.lineplot(data=train_data, x="WeekOfYear", y="Weekly_Sales", ax=ax)
#     # ax.set_xlabel("Week")
#     # ax.set_ylabel("Weekly Sales")
#     # ax.set_title("Trend of Weekly Sales over Time")
#     # st.pyplot(fig3)

#     fig = px.scatter(
#         train_data,
#         x="Size",
#         y="Weekly_Sales",
#         color="Type",
#         labels={"Size": "Store Size", "Weekly_Sales": "Weekly Sales"},
#         title="Weekly Sales vs. Store Size with Store Type",
#     )

#     # Show Plotly chart
#     st.plotly_chart(fig)
#     avg_sales_by_month = (
#         train_data.groupby(["Day", "Month"])["Weekly_Sales"].mean().reset_index()
#     )
#     # Plotly line plot
#     fig = px.line(
#         avg_sales_by_month,
#         x="Day",
#         y="Weekly_Sales",
#         color="Month",
#         labels={"Day": "Day", "Weekly_Sales": "Average Weekly Sales"},
#         title="Average Weekly Sales by Month",
#         color_discrete_map={
#             "January": "blue",
#             "February": "green",
#             "March": "red",
#             # Add more months and corresponding colors as needed
#         },
#     )

#     # Show Plotly chart
#     st.plotly_chart(fig)

#     grouped_data = train_data.groupby("IsHoliday")["Weekly_Sales"]

#     # Create traces for the boxplot
#     data = []
#     for holiday_status, sales in grouped_data:
#         data.append(
#             go.Box(y=sales, name="Holiday" if holiday_status else "Non-Holiday")
#         )

#     # Create layout
#     layout = go.Layout(
#         title="Weekly Sales Distribution for Holidays vs. Non-Holidays",
#         xaxis=dict(
#             title="Is Holiday", tickvals=[0, 1], ticktext=["Non-Holiday", "Holiday"]
#         ),
#         yaxis=dict(title="Weekly Sales"),
#     )

#     # Create figure
#     fig = go.Figure(data=data, layout=layout)

#     # Show Plotly chart
#     st.plotly_chart(fig)


def main():
    st.title("Dashboard")

    # First Row: Average Weekly Sales by Month and Average Weekly Sales by Department
    col1, col2 = st.columns(2)

    # Chart 1: Average Weekly Sales by Month
    with col1:
        # st.write("What is the average weekly sales month-wise?")
        avg_sales_by_month = (
            train_data.groupby("Month")["Weekly_Sales"].mean().reset_index()
        )
        fig1 = px.bar(
            avg_sales_by_month,
            x="Month",
            y="Weekly_Sales",
            title="Average Weekly Sales by Month",
        )
        st.plotly_chart(fig1)

    # Chart 2: Average Weekly Sales by Department
    with col2:
        # st.write("Average Weekly Sales by Department")
        avg_sales_by_store = (
            train_data.sample(1000)
            .groupby(["Dept"])["Weekly_Sales"]
            .mean()
            .reset_index()
        )
        fig2 = px.bar(
            avg_sales_by_store,
            x="Dept",
            y="Weekly_Sales",
            title="Average Weekly Sales by Department",
        )
        fig2.update_layout(
            xaxis_title="Department",
            yaxis_title="Average Weekly Sales",
            xaxis_tickangle=-45,
        )
        st.plotly_chart(fig2)

    # Second Row: Weekly Sales vs. Store Size with Store Type and Weekly Sales Distribution for Holidays vs. Non-Holidays
    col3, col4 = st.columns(2)

    # Chart 3: Weekly Sales vs. Store Size with Store Type
    with col3:
        # st.write("Weekly Sales vs. Store Size with Store Type")
        fig3 = px.scatter(
            train_data,
            x="Size",
            y="Weekly_Sales",
            color="Type",
            labels={"Size": "Store Size", "Weekly_Sales": "Weekly Sales"},
            title="Weekly Sales vs. Store Size with Store Type",
        )
        st.plotly_chart(fig3)

    # Chart 4: Weekly Sales Distribution for Holidays vs. Non-Holidays
    with col4:
        # st.write("Weekly Sales Distribution for Holidays vs. Non-Holidays")
        grouped_data = train_data.groupby("IsHoliday")["Weekly_Sales"]

        # Create traces for the boxplot
        data = []
        for holiday_status, sales in grouped_data:
            data.append(
                go.Box(y=sales, name="Holiday" if holiday_status else "Non-Holiday")
            )

        # Create layout
        layout = go.Layout(
            title="Weekly Sales Distribution for Holidays vs. Non-Holidays",
            xaxis=dict(
                title="Is Holiday", tickvals=[0, 1], ticktext=["Non-Holiday", "Holiday"]
            ),
            yaxis=dict(title="Weekly Sales"),
        )

        # Create figure
        fig4 = go.Figure(data=data, layout=layout)

        # Show Plotly chart
        st.plotly_chart(fig4)

    #     # Show Plotly chart

    avg_sales_by_month = (
        train_data.groupby(["Day", "Month"])["Weekly_Sales"].mean().reset_index()
    )
    # Plotly line plot
    fig = px.line(
        avg_sales_by_month,
        x="Day",
        y="Weekly_Sales",
        color="Month",
        labels={"Day": "Day", "Weekly_Sales": "Average Weekly Sales"},
        title="Average Weekly Sales by Month",
        color_discrete_map={
            "January": "blue",
            "February": "green",
            "March": "red",
            # Add more months and corresponding colors as needed
        },
    )

    # Show Plotly chart
    st.plotly_chart(fig)


if __name__ == "__main__":
    main()
