
import pandas as pd

#Load the dataset
data = pd.read_csv('train.csv')

#Drop columns not useful for analysis
data = data.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'], errors='ignore')

#Handle missing values
data['Age'] = data['Age'].fillna(data['Age'].median())  # Fill Age with median
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])  # Fill Embarked with mode
if 'Fare' in df.columns:
    data['Fare'] = data['Fare'].fillna(data['Fare'].median())  # Fill Fare if missing

#Save cleaned dataset
data.to_csv('titanic_cleaned.csv', index=False)

print("✅ Titanic dataset cleaned and saved as 'titanic_cleaned.csv'")
