import pandas as pd

df = pd.read_csv('19.05.21.csv', sep=';', error_bad_lines=False)
print(df)
