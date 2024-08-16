""" Display Interactive Technical Test
"""

from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
import requests

# Set the path to the datasets directory
datasets_location = Path(__file__).parent / "data"

def read(data1, data2):
    
    # Check if the datasets exists
    if not ((datasets_location / data1 ).exists() or (datasets_location / data2 ).exists()):
        print(f"please include both {data1} and {data2} files in the data folder.")
        exit(1)

    # Load the datasets
    customer_df = pd.read_csv(datasets_location / data1, delimiter=";")
    purchases_df = pd.read_csv(datasets_location / data2, delimiter=";")

    return customer_df, purchases_df

def clean_merge(data1, data2):
    
    # Add a new colum for male and female : Column for salutations
    data1 = data1.assign(
    civility = lambda x: x['title'].map({1: 'Male', 2: 'Female'}).fillna(''),
    salutation = lambda x: x['title'].map({1: 'Mr', 2: 'Mrs'}).fillna(''))

    # Update the currency to fit the schema
    data2 = purchases_df.assign(currency = lambda x: x['currency'].map({'EUR': 'euro', 'USD': 'dollars'}))

    # Merge on purchase because a customer can have 0 or n purchases
    return pd.merge(data1, data2, on='customer_id', how='right')





