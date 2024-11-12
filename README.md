🚀 Data Processor Django Project
Welcome to the Data Processor Django Project! This project processes CSV files in an ETL (Extract, Transform, Load) workflow using Django, PostgreSQL, and Python libraries such as pandas. The system reads data from CSV files, cleans and transforms it, and loads it into a PostgreSQL database. Users can interact with the data through specific endpoints provided by Django views.

📑 Table of Contents
Features
Setup and Installation
Clone the Repository
Set Up a Virtual Environment
Install Requirements
Configure the Database
Run the Django Server
Endpoints
Additional Resources
✨ Features
ETL Process for CSV Data: Reads, cleans, and loads data from CSV files into a PostgreSQL database.
Database-Driven: Uses PostgreSQL to store and manage processed data.
Modular Views: Dedicated endpoints for various data interactions.
Environment Variable Configuration: Securely stores sensitive database credentials in environment variables.
⚙️ Setup and Installation
1. Clone the Repository
Start by cloning the repository to your local machine:

bash
Copy code
git clone https://github.com/waitambatha/csv.git
cd csv
2. Set Up a Virtual Environment
It’s recommended to use a virtual environment to keep dependencies isolated:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On macOS and Linux
venv\Scripts\activate     # On Windows
3. Install Requirements
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
4. Configure the Database
This project uses PostgreSQL. Set up your database credentials securely with a .env file.

Create a .env file in the root of the project and add your PostgreSQL details:

plaintext
Copy code
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
Update settings.py in the project to read from .env:

python
Copy code
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'electric_vehicle_db'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'masterclass'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
This configuration will use your .env file values or the default values if not specified.

5. Run the Django Server
After setting up, start the Django server to access the application:

bash
Copy code
python manage.py runserver
By default, the server will be running at http://127.0.0.1:8000/.

🔗 Endpoints
Here are the available endpoints for data interaction:

Get CSV Data: Retrieve data from a CSV file.

URL: http://127.0.0.1:8000/get_csv/
View: GetCSVData.as_view()
Name: get_csv_data
Insert CSV Data: Insert data from a CSV file into the database.

URL: http://127.0.0.1:8000/insert_csv/
View: InsertCSVData.as_view()
Name: insert_csv_data
Get Electric Vehicle Data: Retrieve electric vehicle data from the database.

URL: http://127.0.0.1:8000/get_electric_vehicle_data/
View: GetElectricVehicleData.as_view()
Name: get_electric_vehicle_data
📂 Additional Resources
Project Documentation: GitHub README.md
Output Screenshots: Output Folder
Source Data: Resources Folder
Sample .env File: Sample Env
Configuration Template: config.py






