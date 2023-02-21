import pandas as pd
import sys
sys.path.insert(0, '.')
df = pd.read_csv("Student_project/data_raw/StudentsPerformance.csv")
print(df.columns)
df.to_csv("Student_project/clean_data/Clean_data.csv",index=False)
print(df)