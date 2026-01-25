import pandas as pd
import numpy as np
from numpy.linalg import matrix_rank
file_path="Lab Session Data.xlsx"
df=pd.read_excel(file_path,sheet_name="Purchase data")
X=df[["Candies (#)","Mangoes (Kg)","Milk Packets (#)"]].to_numpy()
Y=df[["Payment (Rs)"]].to_numpy()
A=df[["Candies (#)","Mangoes (Kg)","Milk Packets (#)","Payment (Rs)"]].to_numpy()
rank_X=matrix_rank(A)
cost=np.linalg.pinv(X)@Y
print("Rank of the matrix:",rank_X)
print("Cost of the Candies:",cost[0][0])
print("Cost of the Mangoes:",cost[1][0])
print("Cost of the Milk products:",cost[2][0])



