# bigquery-data-ingestion
bigquery-data-ingestion
This project automates the process of moving data from Kaggle to Google Cloud Storage (GCS) and then into BigQuery for analysis. It simplifies data retrieval, storage, and loading into BigQuery tables.

Project Overview

kaggle_to_gcs.py: Fetches data from Kaggle and uploads it to GCS.

load_to_bigquery_dag.py: Loads data from GCS into BigQuery tables.

Prerequisites

Kaggle API Key: Download your kaggle.json file from Kaggle and save it securely.

Google Cloud Credentials: Set up a GCP project and download a service account key file.

Python Environment: Install required libraries.

How to Use

Run kaggle_to_gcs.py to download a Kaggle dataset and upload it to GCS:

python kaggle_to_gcs.py

Run load_to_bigquery_dag.py to load the data from GCS into BigQuery:

python load_to_bigquery_dag.py

Future Enhancements

Add data transformation steps for cleaning and preprocessing.

Automate the entire pipeline with Apache Airflow.

Integrate error handling and logging for better monitoring.

Add support for additional data sources beyond Kaggle.
