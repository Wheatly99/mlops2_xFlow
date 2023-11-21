from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("train_model")

train = pd.read_excel('/home/ubuntu/projects/mlops2_xFlow/train.xlsx')

model = RandomForestClassifier(n_estimators=200, max_depth=5, random_state=42)

with mlflow.start_run():

  mlflow.sklearn.log_model(model,
                           artifact_path="rf",
                           registered_model_name="rf")

  mlflow.log_artifact(local_path="/home/ubuntu/projects/mlops2_xFlow/create_model.py",
  artifact_path="train_model code")
  mlflow.end_run()

X_train = train.drop(columns={'Survived'})
y_train = train.Survived

model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')
