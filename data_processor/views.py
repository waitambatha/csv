from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import dask.dataframe as dd
from sqlalchemy import create_engine
from django.conf import settings
from .models import ElectricVehicle
from .serializers import ElectricVehicleSerializer

class ProcessCSVData(APIView):
    def post(self, request):
        # Load the CSV file using Dask
        file_path = '/mnt/data/Electric_Vehicle_Population_Data.csv'
        df = dd.read_csv(file_path)

        # Convert to Pandas DataFrame for insertion
        df = df.dropna().compute()

        # Database connections
        mysql_engine = create_engine('mysql+pymysql://user:password@localhost/your_mysql_db')
        postgres_engine = create_engine('postgresql://user:password@localhost/your_postgres_db')

        # Insert data into MySQL and PostgreSQL
        df.to_sql('data_processor_electricvehicle', mysql_engine, if_exists='replace', index=False)
        df.to_sql('data_processor_electricvehicle', postgres_engine, if_exists='replace', index=False)

        return Response({"message": "Data processed and inserted successfully"}, status=status.HTTP_201_CREATED)
