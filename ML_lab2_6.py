import numpy as np
import pandas as pd
from numpy.linalg import norm
file_path="Lab Session Data.xlsx"
df=pd.read_excel(file_path,sheet_name="thyroid0387_UCI")
df=df.replace({'t':1,'f':0})
df_numeric=df.select_dtypes(include='number')
V1=df_numeric.iloc[0].to_numpy()
V2=df_numeric.iloc[1].to_numpy()
cosine_similarity=np.dot(V1,V2)/norm(V1)*norm(V2)
print("Cosine Similarity:",cosine_similarity)
