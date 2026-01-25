import pandas as pd
import numpy as np
file_path="Lab Session Data.xlsx"
df=pd.read_excel(file_path,sheet_name="Purchase data")
X=df[["Candies (#)","Mangoes (Kg)","Milk Packets (#)"]].to_numpy()
Y=df[["Payment (Rs)"]].to_numpy()
A=df[["Candies (#)", "Mangoes (Kg)","Milk Packets (#)","Payment (Rs)"]].to_numpy()
df["Status"]=np.where(df["Payment (Rs)"]>200,
            "Rich",
            "Poor")
df = df.drop(columns=[col for col in df.columns if "Unnamed" in col])
print("Modified excel sheet as output")
df.to_excel("Purchase_data_modified.xlsx",index=False)


