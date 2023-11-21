import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

model = joblib.load('/home/ubuntu/projects/mlops2_xFlow/model.pkl')

val = pd.read_excel('/home/ubuntu/projects/mlops2_xFlow/test.xlsx')

X_val = val.drop(columns={'Survived'})
y_val = val.Survived

prediction = model.predict(X_val)
print(accuracy_score(prediction, y_val))
