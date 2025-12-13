from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'mlops-team',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'model_training_pipeline',
    default_args=default_args,
    description='Orchestrate Model Training via Airflow',
    schedule_interval='@daily', # Run once a day (after data ingestion)
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # 1. Install Dependencies (In case the Airflow container doesn't have them)
    # Ideally, you'd build a custom Docker image for Airflow with these pre-installed
    install_deps = BashOperator(
        task_id='install_requirements',
        bash_command='pip install torch transformers pandas scikit-learn mlflow accelerate'
    )

    # 2. Run the Training Script
    # Note: We assume your project root is mounted to /opt/airflow/
    train_model = BashOperator(
        task_id='run_training_script',
        bash_command='python /opt/airflow/src/model/train.py',
    )

    install_deps >> train_model