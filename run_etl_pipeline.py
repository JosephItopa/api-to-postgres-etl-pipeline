from extract import extract_data
from transform import transformation
from load import load_to_database
import os

# extract credentials
UIDD = os.get("DB_USER")
PWDD = os.get("DB_PASS")
DSERVER = os.get("DB_HOST")
DPORT = os.get("DB_PORT")
DDB = os.get("DB_NAME")
CSV_URL = os.getenv('CSV_URL')

# run pipeline
df = extract_data(CSV_URL) # extract data
dft = transformation(df) # transform data
load_to_database(dft, UIDD, PWDD, DSERVER, DPORT, DDB) # load data to the database




