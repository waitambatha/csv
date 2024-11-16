# Electric Vehicle Data Visualization

This is a **Streamlit application** for visualizing electric vehicle data stored in a PostgreSQL database. The app connects to the database, retrieves data from the `ElectricVehicle` table, and displays it with interactive charts and graphs.

---

## Features

- Display a sample of electric vehicle data.
- Visualize data through:
  - Bar charts
  - Histograms
  - Pie charts
  - Scatter plots
  - Line charts
- Sidebar options to toggle visualizations.
- Easy-to-use interface for exploring and analyzing electric vehicle data.

---

## Prerequisites

- Python 3.8 or later
- PostgreSQL database with the `ElectricVehicle` table:
  ```sql
  CREATE TABLE ElectricVehicle (
      vin VARCHAR PRIMARY KEY,
      make VARCHAR(100),
      model VARCHAR(100),
      model_year INTEGER,
      vehicle_type VARCHAR(100),
      location VARCHAR(100)
  );

Setup Guide
1. Clone the Repository

git clone https://github.com/waitambatha/csv.git
cd csv/streamlit

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install Dependencies

Install the required Python libraries:

pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the streamlit directory and add your PostgreSQL database credentials:

DB_NAME=electric_vehicle_db
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432

Replace your_postgres_user and your_postgres_password with your actual PostgreSQL credentials.
Running the App

Start the Streamlit app with the following command:

streamlit run streamlit_app.py

Once the app is running, open the provided local URL (e.g., http://localhost:8501) in your browser.
Visualization Options

    Vehicle Make Distribution: A bar chart showing the number of vehicles by make.
    Model Year Distribution: A histogram of vehicle model years.
    Vehicle Type Distribution: A pie chart of vehicle types.
    Model Year by Location: A scatter plot showing model years across locations, categorized by make.
    Model Year Trends: A line chart showing trends in model year frequencies.

Toggle these options using the sidebar.
Example Output

Troubleshooting

    Missing Packages: Ensure all dependencies are installed with pip install -r requirements.txt.
    Database Connection Error: Verify your .env file contains correct PostgreSQL credentials.
    ModuleNotFoundError: Install any missing packages (e.g., plotly) using pip install package_name.

