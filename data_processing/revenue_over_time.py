"""
https://platform.stratascratch.com/coding/10314-revenue-over-time?code_type=2
"""

import numpy as np
import pandas as pd
from itertools import product


def rolling_rev(x: pd.Series):
    rolling_mean = x.rolling(window=3).mean()
    return np.nanmax(rolling_mean)


df = pd.read_csv('./uk_retailer_data.csv', sep=',', encoding='unicode_escape')
df['InvoiceDateTime_pd'] = pd.to_datetime(df['InvoiceDate'])
min_year = min(df['InvoiceDateTime_pd'].dt.year)
max_year = max(df['InvoiceDateTime_pd'].dt.year)
full_months_range = pd.date_range(start=f'1/1/{min_year}', end=f'31/12/{max_year}', freq='MS')
customer_ids = np.unique(df['CustomerID'])
full_cid_date_range = pd.DataFrame.from_records(list(product(customer_ids, full_months_range)),
                                                columns=['CustomerID', 'Month-Year']).sort_values(
    by=['CustomerID', 'Month-Year'], ascending=True)
df['InvoiceDateTime_Month_Year'] = df['InvoiceDateTime_pd'].apply(lambda x: pd.to_datetime(f'{x.year}-{x.month}-01'))

# df.to_csv('./tmp2.csv', index=False, sep=',')
df['tot_revenue'] = df['Quantity'] * df['UnitPrice']

df_agg1 = df.groupby(by=['CustomerID', 'InvoiceDateTime_Month_Year'], as_index=False).agg(
    agg_revenue=pd.NamedAgg(column='tot_revenue', aggfunc='sum')).sort_values(
    by=['CustomerID', 'InvoiceDateTime_Month_Year'])
df_agg1.to_csv('./tmp2.csv', index=False, sep=',')
u = pd.merge(left=df_agg1, right=full_cid_date_range, left_on=['CustomerID', 'InvoiceDateTime_Month_Year'],
             right_on=['CustomerID', 'Month-Year'], how='right')

df2 = u[['CustomerID', 'Month-Year', 'agg_revenue']].sort_values(by=['CustomerID', 'Month-Year'])
df2['agg_revenue'].fillna(0, inplace=True)
df3 = df2.groupby(by='CustomerID',as_index=False).agg(rolling_avg=pd.NamedAgg(column='agg_revenue', aggfunc=rolling_rev))
print('-----')
# TODO
# 1) make aux table with customer id and months from jan - min_year to dec - max_year
# 2) Join to fill time gaps
# 3) fill nan avg revenue with zero
# 4) add agg function that sorts by time and run rolling average
