import pandas as pd
import numpy as np
file_path="Lab Session Data.xlsx"
df=pd.read_excel(file_path,sheet_name="thyroid0387_UCI")
df.replace("?",np.nan,inplace=True)
df=df.infer_objects(copy=False)
numeric_columns=["TSH","T3","TT4","T4U","FTI","TBG"]
for col in numeric_columns:
    df[col]=pd.to_numeric(df[col],errors="coerce")
df.replace({'t':1,'f':0},inplace=True)
numeric_data=df.select_dtypes(include=[np.number])
print("Range of Numeric Attributes:")
for col in numeric_data.columns:
    print(col,"Min:",numeric_data[col].min(),"Max:",numeric_data[col].max())
print("Mean and Variance of Numeric Attributes:")
for col in numeric_data.columns:
    print(col,"Mean:",numeric_data[col].mean(),"Variance:",numeric_data[col].var())
    
    
   
