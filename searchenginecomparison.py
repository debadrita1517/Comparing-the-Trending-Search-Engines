import pandas as pd 
df=pd.read_csv('https://raw.githubusercontent.com/debadrita1517/Comparing-the-Trending-Search-Engines/main/dataset.csv',parse_dates=['Month'],index_col ='Month')
df.info()
df.plot()
df.head(10)
rolling_six=df.rolling(window=6).mean()
rolling_six.head(10)
rolling_six.plot()
pct_change_quarterly=df.pct_change(3)*100
pct_change_quarterly
pct_change_quarterly=pct_change_quarterly.loc['2009':]
pct_change_quarterly.plot(subplots=True,figsize=(12,8))
chrome_trends=pd.DataFrame()
for year in ['2009','2012','2015','2018']:
    chrome_trend_per_year = df.loc[year,['Google Chrome']].reset_index(drop=True)
    chrome_trend_per_year.rename(columns={'Google Chrome':year},inplace=True)
    chrome_trends = pd.concat([chrome_trends,chrome_trend_per_year],axis=1)
    print(chrome_trends)
chrome_trends.plot()
