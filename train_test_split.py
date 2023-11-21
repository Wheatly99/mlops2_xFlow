from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_excel('/home/ubuntu/projects/mlops2_xFlow/data.xlsx')

train = df[df.Survived.notnull()][['Survived', 'Pclass', 'Sex', 'Age',	'Fare', 'FamilySize']]
test = df[df.Survived.isnull()][['Pclass', 'Sex', 'Age',	'Fare', 'FamilySize']]

X = train.drop(columns={'Survived'})
y = train.Survived

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = 0.15, stratify=y)

pd.concat([X_train, y_train], axis=1).to_excel('/home/ubuntu/projects/mlops2_xFlow/train.xlsx', index=False)
pd.concat([X_val, y_val], axis=1).to_excel('/home/ubuntu/projects/mlops2_xFlow/test.xlsx', index=False)
