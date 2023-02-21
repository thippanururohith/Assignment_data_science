import pandas as pd
import sys
sys.path.insert(0, '.')
df = pd.read_csv("Frailty_project/data_raw/raw_frailty_data.csv")
print(df.columns)
df=df[df['Frailty']=='Y']
df.to_csv("Frailty_project/data_clean/Clean_Fraility_data.csv",index=False)
print(df)