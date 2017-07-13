import pandas as pd
from pprint import *
df= pd.read_csv('/Users/apple/Downloads/CommunityOverview.csv',encoding='utf-8')
df=df.loc[:,['群名','入群人数','退群人数','在线用户数','互动用户数','互动用户率','互动次数']]
xc=df[df['群名'].str.contains(".+S.+优达学城$")]
zs=df[df['群名'].str.contains('正式学员')]
tg=df[df['群名'].str.contains("优等生$")]
hz=df[df['群名'].str.contains("Union A")]
dand=df[df['群名'].str.contains("数据分析")]
ipnd=df[df['群名'].str.contains("编程入门")]
fend=df[df['群名'].str.contains("前端开发")]
mlnd=df[df['群名'].str.contains("机器学习")]
dlnd=df[df['群名'].str.contains("深度学习")]
andr=df[df['群名'].str.contains("安卓")]


groups=[xc,zs,tg,hz,dand,fend,ipnd,mlnd,dlnd,andr]


for i in groups:
    print(len(i),i['入群人数'].sum(),i['退群人数'].sum(),i['在线用户数'].sum(),i['互动用户数'].sum(),i['互动用户率'].mean().round(2),i['互动次数'].sum())

growths=df.loc[:,['群名','入群人数']]

# python3 weekly.py | pbcopy- 别名wkl
