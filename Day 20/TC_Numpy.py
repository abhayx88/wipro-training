import numpy as np
import pandas as pd
arr=np.array([10,20,5,6,200])

print("array",arr)
print("sun",np.sum(arr))
print("mean",np.mean(arr))
print("multiply by 2:", arr*2)

data={
    "Name":["Aniket","Abhay","Manish"],
    "Age":[21,22,23],
    "City":["Jhansi","Orai","Indore"]
}

df=pd.DataFrame(data)
print(df)

print(df["Name"])

print([df["Age"]>21])

print(df["City"])