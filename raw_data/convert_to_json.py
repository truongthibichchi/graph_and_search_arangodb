import pandas as pd

df = pd.read_csv('users.csv')
data = df.to_json(orient='records')
with open('users.json', mode='w') as file:
    file.write(data)
