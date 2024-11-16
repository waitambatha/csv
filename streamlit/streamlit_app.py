import streamlit as st
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import plotly.express as px

# Load environment variables for database credentials
load_dotenv()

# Database connection settings from environment variables
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Database connection URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Connect to PostgreSQL
engine = create_engine(DATABASE_URL)

# Streamlit app
st.title("Electric Vehicle Data Visualization")

def load_data(query):
    with engine.connect() as connection:
        data = pd.read_sql(query, connection)
    return data

# Query data
query = "SELECT * FROM ElectricVehicle"
data = load_data(query)

if not data.empty:
    st.write("### Electric Vehicle Data")
    st.write(data.head())  # Display a sample of the data

    # Visualization options
    st.sidebar.header("Choose Visualization")

    # Bar chart of vehicle makes
    if st.sidebar.checkbox("Show Vehicle Make Distribution"):
        make_counts = data['make'].value_counts()
        st.write("### Vehicle Make Distribution")
        fig = px.bar(make_counts, x=make_counts.index, y=make_counts.values, labels={'x': 'Make', 'y': 'Count'})
        st.plotly_chart(fig)

    # Histogram of model year distribution
    if st.sidebar.checkbox("Show Model Year Distribution"):
        st.write("### Model Year Distribution")
        fig = px.histogram(data, x='model_year', nbins=20, labels={'model_year': 'Model Year'})
        st.plotly_chart(fig)

    # Pie chart of vehicle types
    if st.sidebar.checkbox("Show Vehicle Type Distribution"):
        vehicle_type_counts = data['vehicle_type'].value_counts()
        st.write("### Vehicle Type Distribution")
        fig = px.pie(vehicle_type_counts, names=vehicle_type_counts.index, values=vehicle_type_counts.values)
        st.plotly_chart(fig)

    # Scatter plot of Model Year vs. Location
    if st.sidebar.checkbox("Show Model Year by Location"):
        st.write("### Model Year by Location")
        fig = px.scatter(data, x='location', y='model_year', color='make', hover_data=['vin', 'model'])
        st.plotly_chart(fig)

    # Line chart of model year trends (assuming data for multiple years)
    if st.sidebar.checkbox("Show Model Year Trends"):
        st.write("### Model Year Trends")
        year_counts = data['model_year'].value_counts().sort_index()
        fig = px.line(year_counts, x=year_counts.index, y=year_counts.values, labels={'x': 'Model Year', 'y': 'Number of Vehicles'})
        st.plotly_chart(fig)

else:
    st.write("No data found in the database.")
