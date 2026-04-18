import pandas as pd

df = pd.read_csv("data.csv") 
print(df)

disease_count = df['disease'].value_counts()
print(disease_count)

cost_stats = df['treatment_cost'].describe()
print(cost_stats)

doctor_group = df.groupby('doctor').size()
print(doctor_group)