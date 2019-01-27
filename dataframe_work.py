from collections import defaultdict
import pandas as pd


the_dict=defaultdict(int)
df=pd.read_csv('national_features.csv')

c_l=list(df['countries'])



for item in c_l:
    if item in the_dict:
        pass
    else:
        the_dict[item]=0

#df2=df.iloc[[df.loc[:,'countries']=='burma']]

df2=df.loc[df.iloc[:,0]=='korea',:]
df3=df2.loc[df2['feature'].isin(['big nose'])]
print(df3['value'])
print(str(df3['value']))
#все строки, где столбец равен значению feature= big nose

df3.to_csv('practise.csv')

# первая колонка - data.iloc[:,0]