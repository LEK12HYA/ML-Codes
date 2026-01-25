import pandas as pd
import numpy as np
file_path="Lab Session Data.xlsx"
df=pd.read_excel(file_path,sheet_name="thyroid0387_UCI")
row1=df.iloc[0]
row2=df.iloc[1]
binary_cols=[]
for col in df.columns:
    unique_values=df[col].dropna().unique()
    if len(unique_values)==2:
        binary_cols.append(col)
print("Binary Columns:",binary_cols)
df[binary_cols]=df[binary_cols].replace({'t':1,'f':0})
v1=df.loc[0,binary_cols]
v2=df.loc[1,binary_cols]
f11=sum((v1==1)&(v2==1))
f00=sum((v1==0)&(v2==0))
f10=sum((v1==1)&(v2==0))
f01=sum((v1==0)&(v2==1))
print(f11,f00,f10,f10)
JC=f11/(f01+f10+f11)
SMC=(f11+f00)/(f00+f01+f10+f11)
print("Jaccard Coefficient:",JC)
print("Simple Matching Coefficient:",SMC)
