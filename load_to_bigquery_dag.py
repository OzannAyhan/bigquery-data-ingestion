import os
from google.cloud import bigquery


# Create dataset folder under project in big query by using => bq --location=US mk -d static-lens-448507-j9:covid_dataset


# Set Google Cloud authentication for BigQuery
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\HUAWEI\Desktop\Covid Project\service-account-key.json"

def load_csv_to_bigquery(bucket_name, file_name, dataset_id, table_id):
    """Loads a CSV file from GCS to BigQuery."""
    
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    uri = f"gs://{bucket_name}/{file_name}"  # GCS file path

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )

    print(f"Loading {file_name} into BigQuery table {dataset_id}.{table_id}...")

    load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)
    load_job.result()  # Wait for the job to complete

    print(f"✅ Loaded {file_name} into {dataset_id}.{table_id} successfully!")

def upload_all_csv_to_bigquery(bucket_name, dataset_id):
    """Loads all CSV files from GCS to BigQuery with new table names."""
    
    # List of all CSV files uploaded to GCS
    csv_files = [
        "country_wise_latest.csv",
        "covid_19_clean_complete.csv",
        "day_wise.csv",
        "full_grouped.csv",
        "usa_county_wise.csv"
    ]
    
    for file_name in csv_files:
        # Generate a new table name based on the file name
        table_id = file_name.replace(".csv", "").replace("-", "_").replace(" ", "_")
        
        print(f"Processing file: {file_name} -> Table: {table_id}")
        load_csv_to_bigquery(bucket_name, file_name, dataset_id, table_id)

# Example Usage
bucket_name = "test-data-buckett"
dataset_id = "covid_dataset"

upload_all_csv_to_bigquery(bucket_name, dataset_id)
