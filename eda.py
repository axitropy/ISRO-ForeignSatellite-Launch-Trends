import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# loading the cleaned data
df = pd.read_csv('cleaned_satellite_data.csv')

# analyzing trends in payload types over time
# identifying the most frequently used launch vehicles
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='launch_vehicle', order=df['launch_vehicle'].value_counts().index)
plt.title('Most Frequently Used Launch Vehicles')
plt.xticks(rotation=45)
plt.show()

# analyzing the number of launches per year
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='year', order=df['year'].sort_values().unique())
plt.title('Number of Launches Per Year')
plt.xticks(rotation=45)
plt.show()

# analyzing the distribution of launch mass
plt.figure(figsize=(10, 6))
sns.histplot(df['launch_mass'].dropna(), bins=20, kde=True)
plt.title('Distribution of Launch Mass')
plt.xlabel('Launch Mass (kg)')
plt.show()





