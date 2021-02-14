import pandas as pd 

"""
function that reads a csv, and when the first line or header
turns into numbers, read as next line.
"""

"""Function that divides the first line into two rows"""

header_list = [i for i in range(1,20)]
data = pd.read_csv("dataset tempMod CO_RH/20161016_053656.csv",nrows=1)
data1 = data.iloc[0,:20].to_frame()

data = pd.read_csv("dataset tempMod CO_RH/20161016_053656.csv")
data2 = data.iloc[:,:20]

#print(data2)
print(pd.concat([data1.transpose(),data2]))
#print(data2)
#data1 = data.iloc[0,:20]
"""print(data1)
print(data2)
data3 = data.iloc[1:,:20]
#print(data3)
print(pd.concat([data1,data2,data3], axis=0))"""