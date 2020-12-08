from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Déborah Mesquita',
    'start_date': days_ago(1)
    }

# Defining the DAG using Context Manager
with DAG(
        'extract-meeting-activities',
        default_args=default_args,
        schedule_interval=None,
        ) as dag:
        t1 = BashOperator(
                task_id = 'extract_text_from_pdf',
                bash_command = '/YOUR-LOCAL-PATH/airflow-tutorial/first-workflow/pdf_to_text.sh {{ dag_run.conf["pdf_filename"] if dag_run else '' }}',
        )

        t2 = BashOperator(
                task_id = 'extract_metadata_from_text',
                bash_command = 'python3 /YOUR-LOCAL-PATH/airflow-tutorial/first-workflow/extract_metadata.py',
        )

        t1 >> t2 # Defining the task dependencies
