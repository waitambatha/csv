import dask.dataframe as dd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine, text
from django.conf import settings
from .models import ElectricVehicle
from .serializers import ElectricVehicleSerializer
import os

class GetCSVData(APIView):
    def get(self, request):
        # Load the CSV file using Dask
        file_path = 'Electric_Vehicle_Population_Data.csv'

        dtype = {
            '2020 Census Tract': 'float64',
            'Base MSRP': 'float64',
            'Electric Range': 'float64',
            'Legislative District': 'float64',
            'Postal Code': 'float64',
        }

        # Reading the CSV file with Dask
        df = dd.read_csv(file_path, dtype=dtype)
        df = df.compute()  # Convert Dask DataFrame to Pandas DataFrame

        # Get the first 15 rows of the dataframe
        sample_df = df.head(15)

        # Return the first 15 rows in the response
        return Response({
            "message": "CSV loaded successfully. First 15 rows are shown below.",
            "data": sample_df.to_dict(orient="records"),  # Convert to dictionary format
            "instructions": "To push the entire data to PostgreSQL, send a POST request to /api/insert_csv/"
        })



class InsertCSVData(APIView):
    def post(self, request):
        try:
            # Load the CSV file
            file_path = 'Electric_Vehicle_Population_Data.csv'
            df = pd.read_csv(file_path)

            # Strip whitespace from column names
            df.columns = df.columns.str.strip()

            # Define expected columns
            expected_columns = [
                'vin', 'make', 'model', 'model_year', 'vehicle_type',
                'location'
            ]

            # Filter to expected columns only
            df = df[expected_columns]

            # Remove duplicate VINs
            df = df.drop_duplicates(subset=['vin'])

        
            # Connect to the PostgreSQL database
            postgres_engine = create_engine('postgresql://postgres:masterclass@localhost/electric_vehicle_db')

            # Insert data into database
            df.to_sql('electricvehicle', postgres_engine, if_exists='append', index=False)

            return Response({"message": "Data processed and inserted successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"message": f"Error inserting data: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)



class ViewDatabaseData(APIView):
    def get(self, request):
        try:
            # Retrieve data from the database
            vehicles = ElectricVehicle.objects.all()

            # Serialize the data using the ElectricVehicleSerializer
            serializer = ElectricVehicleSerializer(vehicles, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": f"Error retrieving data from database: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
class GetElectricVehicleData(APIView):
    def get(self, request):
        # Database connection to PostgreSQL
        postgres_engine = create_engine('postgresql://postgres:masterclass@localhost/electric_vehicle_db')

        try:
            # Query the data from the 'ElectricVehicle' table
            query = "SELECT * FROM ElectricVehicle"
            df = pd.read_sql(query, postgres_engine)

            # Convert the dataframe to a dictionary format to return as JSON
            data = df.to_dict(orient="records")

            return Response({
                "message": "Data fetched successfully from PostgreSQL",
                "data": data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": f"Error fetching data: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)