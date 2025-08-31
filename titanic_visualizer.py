
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv('titanic_cleaned.csv')

# Set style
sns.set_style('whitegrid')

# Survival Count Plot
plt.figure(figsize=(6,4))
sns.countplot(x='Survived', data=df, palette='Blues')
plt.title('Survival Count (0 = No, 1 = Yes)')
plt.savefig('survival_count.png')
plt.close()

# Survival by Gender
plt.figure(figsize=(6,4))
sns.countplot(x='Sex', hue='Survived', data=df, palette='Set2')
plt.title('Survival by Gender')
plt.savefig('survival_by_gender.png')
plt.close()

# Survival by Class
plt.figure(figsize=(6,4))
sns.countplot(x='Pclass', hue='Survived', data=df, palette='Set1')
plt.title('Survival by Passenger Class')
plt.savefig('survival_by_class.png')
plt.close()

# Age Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins=30, kde=True, color='purple')
plt.title('Age Distribution of Passengers')
plt.savefig('age_distribution.png')
plt.close()

print("✅ Visualizations saved: survival_count.png, survival_by_gender.png, survival_by_class.png, age_distribution.png")
