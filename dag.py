from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
import datetime as dt

args = {
  "owner": "wheatly",
  "start_date": dt.datetime(2023, 11, 21),
  "retries": 5,
  "retry_delays": dt.timedelta(minutes=1),
  "depends_on_past": False
}

with DAG(
  dag_id='titanic',
  default_args=args,
  schedule_interval=None,
  tags=['score'],
) as dag:

  get_data = BashOperator(task_id='get_data',
                          bash_command="python3 /home/ubuntu/projects/mlops2_xFlow/get_data.py",
                          dag=dag)

  process_data = BashOperator(task_id='process_data',
                              bash_command="python3 /home/ubuntu/projects/mlops2_xFlow/data_prepocessing.py",
                              dag=dag)

  train_test_split_data = BashOperator(task_id='train_test_split',
                                       bash_command="python3 /home/ubuntu/projects/mlops2_xFlow/train_test_split.py",
                                       dag=dag)

  train_model = BashOperator(task_id='train_model',
                             bash_command="python3 /home/ubuntu/projects/mlops2_xFlow/create_model.py",
                             dag=dag)

  test_model = BashOperator(task_id='test_model',
                            bash_command="python3 /home/ubuntu/projects/mlops2_xFlow/test_model.py",
                            dag=dag)

get_data >> process_data >> train_test_split_data >> train_model >> test_model
