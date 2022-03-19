import pandas as pd

csv_file = "election_results.csv"
df_elections = pd.read_csv(csv_file)
print(df_elections.head())

election_data = open(csv_file, 'r')


