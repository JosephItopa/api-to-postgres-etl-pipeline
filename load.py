import os
import time
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# establish connection to database 
def connect_to_db(uidd, pwdd, dserver, dport, ddb):
    return create_engine(f'postgresql://{uidd}:{pwdd}@{dserver}:{dport}/{ddb}')

# ingest data into database
def load_to_database(df, UIDD, PWDD, DSERVER, DPORT, DDB):
    curr = connect_to_db(UIDD, PWDD, DSERVER, DPORT, DDB)
    # Insert DataFrame records one by one.
    for i,row in df.iterrows():
        mod = pd.DataFrame(row.to_frame().T) 
        mod.to_sql("rickyandmorty", con=curr, if_exists='replace', index=False) #'fail', 'replace', 'append'
        time.sleep(1)
    print("loaded table with current data.")


