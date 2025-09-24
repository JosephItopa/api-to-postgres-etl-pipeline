import os
import time
import psycopg2
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text

def connect_to_db():
    conn = psycopg2.connect(database = "postgres",\
                        user = "sakar_",\
                        host = url,\
                        password = "sakar10",\
                        port = 5432)
    return conn

def connect_to_db(uidd, pwdd, dserver, dport, ddb):
    return create_engine(f'postgresql://{uidd}:{pwdd}@{dserver}:{dport}/{ddb}')


def load_to_database(df):
    curr = connect_to_db("postgres", "toor", "localhost", 5432, "postgres")
    # Insert DataFrame recrds one by one.
    for i,row in df.iterrows():
        mod = pd.DataFrame(row.to_frame().T) 
        mod.to_sql("rickyandmorty", con=curr, if_exists='replace', index=False) #'fail', 'replace', 'append'
        time.sleep(1)
    print("loaded table with current data.")


