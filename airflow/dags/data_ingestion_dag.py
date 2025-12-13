from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'mlops_team',
    'start_date': days_ago(1),
    'retries': 1,
}

with DAG(
    dag_id='ecom_data_pipeline',
    default_args=default_args,
    description='Ingests data pipeline',
    schedule_interval='@daily',
    tags=['mlops', 'ecom'],
    catchup=False
) as dag:

    check_data = BashOperator(
        task_id='check_azure_data',
        bash_command='echo "Data confirmed available."',
    )

    process_data = BashOperator(
        task_id='process_data',
        bash_command='echo "Processing products.csv..."',
    )

    check_data >> process_data
