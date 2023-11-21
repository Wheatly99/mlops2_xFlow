from catboost.datasets import titanic
import pandas as pd
import os

import mlflow
from mlflow.tracking import MlflowClient

os.environ["MLFLOW_REGISTRY_URI"] = "/home/ubuntu/mlflow/"
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("get_data")

with mlflow.start_run():

  titanic_train, titanic_test = titanic()
  df = pd.concat([titanic_train, titanic_test], ignore_index=True)

  mlflow.log_artifact(local_path="/home/ubuntu/projects/mlops2_xFlow/get_data.py",
                      artifact_path="get_data code")
  mlflow.end_run()

df.to_excel('/home/ubuntu/projects/mlops2_xFlow/data.xlsx', index=False)

