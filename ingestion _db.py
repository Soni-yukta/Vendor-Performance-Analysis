import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Logging configuration
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(file_path, table_name, engine):
    '''Batch processing: Ye function memory crash hone se bachayega'''
    # chunksize=100000 matlab ek baar mein sirf 1 lakh rows RAM mein aayengi
    first_chunk = True
    for chunk in pd.read_csv(file_path, chunksize=100000):
        if first_chunk:
            # Pehli baar mein purani table 'replace' hogi
            chunk.to_sql(table_name, con=engine, if_exists='replace', index=False)
            first_chunk = False
        else:
            # Baaki saare chunks 'append' honge
            chunk.to_sql(table_name, con=engine, if_exists='append', index=False)
        
        logging.info(f"Chunk processed for {table_name}...")

def load_raw_data():
    start = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            file_path = os.path.join('data', file)
            table_name = file[:-4]
            logging.info(f'--- Starting Ingestion for {file} ---')
            
            # Direct file path bhej rahe hain read_csv ke liye
            ingest_db(file_path, table_name, engine)
            
    end = time.time()
    total_time = (end - start) / 60
    logging.info('--------------------Ingestion Complete--------------------')
    logging.info(f'\nTotal Time Taken: {total_time} minutes')

if __name__ == "__main__":
    load_raw_data()