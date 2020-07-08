# Airflow and TM1 

Proof of concept that demonstrates using a basic custom hook to create a connection to a TM1 database and uses this in an example DAG to extract data from a view and write it as a csv to an S3 bucket

## Requirements

* An Airflow environment with support for S3 and TM1py
* Example DAG depends on connections "s3_default" and "tm1_default"



