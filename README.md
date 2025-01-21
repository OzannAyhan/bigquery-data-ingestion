# BigQuery Data Ingestion Project

This project automates the process of moving data from Kaggle to Google Cloud Storage (GCS) and then into BigQuery for analysis. It simplifies data retrieval, storage, and loading into BigQuery tables.

---

## Project Overview

This repository contains the following key scripts:

- **`kaggle_to_gcs.py`**: Fetches data from Kaggle and uploads it to a specified Google Cloud Storage (GCS) bucket.
- **`load_to_bigquery_dag.py`**: Loads data from GCS into BigQuery tables for analysis.

---

## Prerequisites

To use the scripts, ensure the following:

1. **Kaggle API Key**:
   - Download your `kaggle.json` file from your Kaggle account.
   - Save it in a secure location (e.g., `~/.kaggle/kaggle.json`).

2. **Google Cloud Credentials**:
   - Set up a Google Cloud Platform (GCP) project.
   - Download a service account key file with the required permissions (access to GCS and BigQuery).

3. **Python Environment**:
   - Install the required libraries listed in `requirements.txt`
   - pip install -r requirements.txt

---

## How to Use

Follow these steps to run the pipeline:

1. **Fetch Kaggle Data**:
   - Use `kaggle_to_gcs.py` to download a dataset from Kaggle and upload it to GCS:
     ```bash
     python kaggle_to_gcs.py
     ```

2. **Load Data into BigQuery**:
   - Use `load_to_bigquery_dag.py` to move the data from GCS to BigQuery:
     ```bash
     python load_to_bigquery_dag.py
     ```

---

## Future Enhancements

The project will be extended with the following features:

- **Data Transformation**: Add preprocessing and cleaning steps before loading data into BigQuery.
- **Pipeline Automation**: Integrate Apache Airflow to automate the entire workflow.
- **Monitoring**: Implement error handling and logging for better tracking.
- **New Data Sources**: Add support for ingesting data from sources beyond Kaggle.

---


