import pandas as pd

df = pd.read_csv('foreign_satellites_by_india.csv')

print("Initial DataFrame:")
print(df.head())

df.columns = df.columns.str.lower().str.replace(' ', '_')

# standardizing launch vehicle names
df['launch_vehicle'] = df['launch_vehicle'].str.upper().str.strip()

df.fillna(method='ffill', inplace=True)

df['launch_mass'] = pd.to_numeric(df['launch_mass'], errors='coerce')

df['launch_date'] = pd.to_datetime(df['launch_date'], errors='coerce')

df['year'] = df['launch_date'].dt.year

print("\nCleaned DataFrame:")
print(df.head())

df.to_csv('cleaned_satellite_data.csv', index=False)

print("\nData cleaning complete. Cleaned data saved to 'cleaned_satellite_data.csv'.")






