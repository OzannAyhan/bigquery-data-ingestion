##Will be updated

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

# Define paths to your scripts
KAGGLE_SCRIPT_PATH = "/opt/airflow/scripts/kaggle_to_gcs.py"  # Path inside Docker
BIGQUERY_SCRIPT_PATH = "/opt/airflow/scripts/load_to_bigquery_dag.py"

# Function to execute Kaggle script
def run_kaggle_script():
    os.system(f"python {KAGGLE_SCRIPT_PATH}")

# Function to execute BigQuery script
def run_bigquery_script():
    os.system(f"python {BIGQUERY_SCRIPT_PATH}")

# Default DAG arguments
default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 2, 1),
    "retries": 1,
}

# Define DAG
dag = DAG(
    "Dag1",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
)

# Task 1: Run Kaggle to GCS script
task_1 = PythonOperator(
    task_id="kaggle_to_gcs",
    python_callable=run_kaggle_script,
    dag=dag,
)

# Task 2: Run GCS to BigQuery script
task_2 = PythonOperator(
    task_id="gcs_to_bigquery",
    python_callable=run_bigquery_script,
    dag=dag,
)

# Set dependencies
task_1 >> task_2  # Ensure GCS to BigQuery runs after Kaggle to GCS

