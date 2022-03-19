import pandas as pd
# print(pd.__version__)
csv_file = "election_results.csv"
df_elections = pd.read_csv(csv_file)
print(df_elections.head())


