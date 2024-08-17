""" Display Interactive Technical Test
"""

import sys
from pathlib import Path
import json
import pandas as pd
import requests
import config

log = config.logging
# Set the path to the datasets directory
datasets_location = Path(__file__).parent / "data"


def read(data1, data2):
    """_This functions reads the data from the csv files_

    Arguments:
        data1 -- _customer data_
        data2 -- _purchase data_

    Returns:
        _customer dataframe, purchase dataframe_
    """

    # Check if the datasets exists
    if not (
        (datasets_location / data1).exists() or (datasets_location / data2).exists()
    ):
        log.error(
            "please include both %s and %s files in the data folder.", data1, data2
        )
        sys.exit(1)

    try:
        # Load the datasets
        customer_df = pd.read_csv(datasets_location / data1, delimiter=";")
        purchases_df = pd.read_csv(datasets_location / data2, delimiter=";")
        log.info("Datasets loaded")

    except FileNotFoundError as e:
        log.error("File doesn't exist: %s, Please add this file in the data folder", e)
        sys.exit(1)

    return customer_df, purchases_df


def clean_merge(data1, data2):
    """clean_merge _This function cleans and merges the 2 dataframes_

    Arguments:
        data1 -- _customer data_
        data2 -- _purchase data_

    Returns:
        _Merged Dataframe_
    """

    # Add a new colum for male and female : Column for salutations
    data1 = data1.assign(
        civility=lambda x: x["title"].map({1: "Male", 2: "Female"}).fillna(""),
        salutation=lambda x: x["title"].map({1: "Mr", 2: "Mrs"}).fillna(""),
    )

    # Update the currency to fit the schema
    data2 = data2.assign(
        currency=lambda x: x["currency"].map({"EUR": "euro", "USD": "dollars"})
    )

    # Merge on purchase because a customer can have 0 or n purchases
    return pd.merge(data1, data2, on="customer_id", how="right")


def purchased_objects(data):
    """purchased_objects _This function is formats the purchased objects_

    Arguments:
        data -- _Merged dataframe_

    Returns:
        _List of purchases_
    """
    return data.apply(
        lambda x: {
            "product_id": x["product_id"],
            "price": x["price"],
            "currency": x["currency"],
            "quantity": x["quantity"],
            "purchased_at": x["date"],
        },
        axis=1,
    ).tolist()


def create_payload(data):
    """create_payload _This function creats the JSON payload to send to the API_

    Arguments:
        data -- _dataframe_

    Returns:
        _formated JSON_
    """

    # Format the dataframe into a dictionary and append purchases for each customer
    payload_structure = (
        data.groupby(["customer_id", "salutation", "lastname", "firstname", "email"])
        .apply(purchased_objects, include_groups=False)
        .reset_index(name="purchases")
    )
    payload = payload_structure.to_dict(orient="records")

    for customer in payload:
        del customer["customer_id"]

    return json.dumps(payload, indent=4)


def send_payload(url, json):

    # log.info
    log.info("Sending PUT request to %s", url)

    # Make sure the api knows it is json
    headers = {"Content-Type": "application/json"}
    response = requests.put(url=url, data=json, headers=headers, timeout=10)

    # Print response status code and content
    log.info("Request sent. Status Code: %d", response.status_code)
    log.debug("Response Content: %s", response.content.decode("utf-8"))


if __name__ == "__main__":
    # Run this script with arguments, dataset1 and dataset2
    if len(sys.argv) != 3:
        log.error(
            "Invalid arguements, use customer dataset as the first argument and products dataset as the second arcument"
        )
        sys.exit(1)

    dataset1 = sys.argv[1]
    dataset2 = sys.argv[2]

    # Get the url from the environment variable
    url = config.URL

    customers, purchases = read(dataset1, dataset2)

    merged = clean_merge(customers, purchases)

    payload = create_payload(merged)

    try:
        send_payload(url, payload)
    except requests.exceptions.RequestException as e:
        log.error("Error sending payload: %s", e)
