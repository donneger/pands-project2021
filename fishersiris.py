import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "fishersiris.csv"

workbookfile = "fishers.xlsx"

df = pd.read_excel(workbookfile)

print(df)


#listofcols = ["PW", "SW"]
#df = df.pivot(index="Type", columns=[listofcols], aggfunc=np.sum)
#df.plot.bar()




#df.to_excel(workbookfile, sheet_name = "fishers", index=False)


#print(df.head(5))
#print(df.describe())

#print(df.head(5))
#print(df.tail(5))
#listofcols = ["PW", "SW"]
#df["new"] = df["PW"] * df ["SW"]
#print(df.head(5))
#print(df.describe())
#print(df.duplicated())

