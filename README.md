
Data Processor Django Project
This Django project processes CSV files in an ETL workflow. The project reads data from CSV files, cleans and transforms it, and loads it into a PostgreSQL database. Users can view and manage data through specific endpoints provided by Django views. This guide will walk you through cloning the repository, setting up the environment, configuring the database, and running the Django server.

Table of Contents
Clone the Repository
Set Up a Virtual Environment
Install Requirements
Configure the Database
Run the Django Server
Available Endpoints

Clone the Repository
To start, clone this repository to your local machine:

bash
Copy code
git clone https://github.com/waitambatha/csv.git
Navigate into the project directory:

bash
Copy code
cd csv
Set Up a Virtual Environment
It’s recommended to use a virtual environment to keep dependencies isolated from other projects.

Create a virtual environment:
bash
Copy code
python3 -m venv venv
Activate the virtual environment:
On macOS and Linux:
bash
Copy code
source venv/bin/activate
On Windows:
bash
Copy code
venv\Scripts\activate
Install Requirements
With the virtual environment activated, install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the Database
This project uses PostgreSQL as its database. You need to configure your database settings in settings.py to use your own credentials without hardcoding them. Follow these steps:

Create a .env file in the root of the project with the following variables:

plaintext
Copy code
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_host (e.g., localhost)
DB_PORT=your_port (e.g., 5432)
Update settings.py: The database configuration in settings.py is set to read these values from the .env file as follows:

python
Copy code
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
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
This configuration will use the values in .env or the default values if not specified.

Run the Django Server
Once everything is set up, you can start the Django development server to access the project:

bash
Copy code
python manage.py runserver
The server will start running at http://127.0.0.1:8000/ by default.

Available Endpoints
This project includes the following endpoints:

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
