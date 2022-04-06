import pandas as pd
import numpy as np
print("dataframe")
df=pd.DataFrame()
print(df)
data_dict={"Name":["V","S","R","I"],"Age":[23,45,46,52]}
df=pd.DataFrame(data_dict)
print(df)
print(df.head())


print("Series")
d={0:"Ajay",1:"Jay",2:"Vijay"}
s=pd.Series(d)
print(s)
a=np.array([51,65,48,59,68])
s=pd.Series(a)
print(s)
s=pd.Series(10,index=[0,1,2,3,4,5])
print(s)
df=pd.read_csv("Data/WHO_first9cols.csv")
print(df)
print(df.columns)
cs=df["Country"]
print(cs)
print(df.shape)
print(cs.shape)
print(cs[-5:])

print("annual")
ss=pd.read_csv("Data\AnnualSunspots.csv")
print(ss)
ss_filt1=ss[["Yearly Mean","Indicator"]]
print(ss_filt1.head())
print(ss_filt1.tail())
print(ss[ss["Yearly Mean"]>ss["Yearly Mean"].mean()])

print("Statistics")
print(df.describe())
print(df.count())
print(df.mad())
print(df.median())
print(df.mode())
print(df.min())
print(df.max())
#print(df.std())
#print(df.var())
#print(df.skew())
#print(df.kurt())
print(ss.groupby("Yearly Mean").mean())
print(ss.groupby("Yearly Mean").mean()["Indicator"])
#print(df.groupby("Continent").mean()["Adult literacy rate(%)"])

print("Join")
dest=pd.read_csv("Data/dest.csv")
tips=pd.read_csv("Data/tips.csv")
print(dest)
print(tips)
print(pd.merge(dest,tips,on="EmpNr",how="inner"))
print(pd.merge(dest,tips,on="EmpNr",how="outer"))
print(pd.merge(dest,tips,on="EmpNr",how="left"))
print(pd.merge(dest,tips,on="EmpNr",how="right"))
print(pd.isnull(df).sum())
print(df.dropna(inplace=True))
print(df.info())

print("pivottable")
pc=pd.read_csv("Data\purchase.csv")
print(pc.head())
print(pd.pivot_table(pc,values="Number",index=("Weather",),columns=["Food"],aggfunc=np.sum))

print("Date")
print(pd.date_range("01-01-2000",periods=45,freq="D"))
print(pd.date_range("01-01-2000",periods=45,freq="B"))
print(pd.date_range("01-01-2000",periods=45,freq="W"))
print(pd.date_range("01-01-2000",periods=45,freq="H"))
print(pd.date_range("01-01-2000",periods=45,freq="M"))
print(pd.date_range("01-01-2000",periods=45,freq="S"))
print(pd.date_range("01-01-2000",periods=45,freq="L"))
print(pd.date_range("01-01-2000",periods=45,freq="U"))
print(pd.to_datetime(["20200101", "20200102"], format = "%Y%m%d")
)



