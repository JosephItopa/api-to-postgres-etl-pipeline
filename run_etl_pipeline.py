from extract import extract_data
from transform import transformation
import os

postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_port = os.getenv('POSTGRES_PORT')
postgres_host = os.getenv('POSTGRES_HOST')
postgres_dw = os.getenv('POSTGRES_DW')
csv_url = os.getenv('CSV_URL')

# source export_var.sh

# docker build -t etl_pipeline .



