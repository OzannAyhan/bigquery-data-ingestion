import os
import zipfile
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from google.cloud import storage

# Authenticate with Google Cloud Storage
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\HUAWEI\Desktop\Covid Project\service-account-key.json"

def preprocess_csv(file_path):
    """Preprocess CSV files to make them BigQuery-compatible."""
    df = pd.read_csv(file_path)

    # Rename columns (replace spaces, dots, slashes)
    df.columns = [col.replace(".", "_").replace(" ", "_").replace("/", "_") for col in df.columns]

    # Save the cleaned CSV file
    df.to_csv(file_path, index=False)

def upload_to_gcs_direct(bucket_name, dataset_ref, temp_download_path):
    """Download dataset from Kaggle, preprocess, and upload to GCS."""
    api = KaggleApi()
    api.authenticate()

    client = storage.Client()
    bucket = client.bucket(bucket_name)

    # Step 1: Download the dataset to a temporary location
    print(f"Downloading dataset '{dataset_ref}' from Kaggle...")
    api.dataset_download_files(dataset_ref, path=temp_download_path, unzip=False)
    zip_file_path = os.path.join(temp_download_path, f"{dataset_ref.split('/')[-1]}.zip")

    # Step 2: Extract and preprocess files
    with zipfile.ZipFile(zip_file_path, 'r') as z:
        for file_name in z.namelist():
            extracted_path = os.path.join(temp_download_path, file_name)
            z.extract(file_name, temp_download_path)
            if file_name.endswith('.csv'):
                print(f"Preprocessing {file_name}...")
                preprocess_csv(extracted_path)
            
            # Step 3: Upload preprocessed file to GCS
            print(f"Uploading {file_name} to GCS...")
            blob = bucket.blob(file_name)
            blob.upload_from_filename(extracted_path)
            print(f"Uploaded {file_name} to bucket {bucket_name}.")
    
    # Clean up the temporary zip file
    os.remove(zip_file_path)

# Parameters
bucket_name = "test-data-buckett" # Replace with your GCS bucket name
dataset_ref = "imdevskp/corona-virus-report"  # Kaggle dataset reference
temp_download_path = r"C:\Users\HUAWEI\Desktop\Covid Project\temp"

# Ensure the temporary folder exists
if not os.path.exists(temp_download_path):
    os.makedirs(temp_download_path)

# Run the upload function
upload_to_gcs_direct(bucket_name, dataset_ref, temp_download_path)
