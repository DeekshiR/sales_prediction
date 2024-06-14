import streamlit as st
from predict import main as predict_page
from dashboard import main as dashboard_page

PAGES = {"Dashboard": dashboard_page, "Sales Prediction": predict_page}


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page()


if __name__ == "__main__":
    main()
