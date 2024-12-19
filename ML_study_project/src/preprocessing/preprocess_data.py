import sqlite3
import pandas as pd


# -- PREPROCESSING -- #

# Defining paths
db_path = '../../data/raw/study_data.db'
output_csv_path = '../../data/processed/processed_study_data.csv'

# Connect to SQlite database
connection = sqlite3.connect(db_path)

# Load study_hours table into a Pandas dataframe
query = "SELECT * FROM study_hours"
df = pd.read_sql_query(query, connection)

#closing the database connection
connection.close()


# -- FEATURE ENGINEERING -- #

#calculate weekly totals
weekly_totals = df.groupby('week')['hours'].sum().reset_index()
weekly_totals.rename(columns={'hours': 'week_total'}, inplace=True)

# Merge weekly totals into the main dataframe
df = df.merge(weekly_totals, on='week')

# Save the processed dataframe to a csv file
df.to_csv(output_csv_path, index=False)

print(f'Processed data saved to {output_csv_path}')