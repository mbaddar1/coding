"""
https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=2
"""
import numpy as np
import pandas as pd


def max_days(x: pd.Series) -> int:
    x.sort_values(inplace=True)
    x = pd.Series(pd.to_datetime(np.unique(x.dt.date)))
    diff_ = x.diff()
    diff_days = diff_.apply(lambda x: x.days)
    max_diff = np.nanmax(diff_days)  # nan in diff

    return max_diff


df = pd.read_csv('./uk_retailer_data.csv', sep=',', encoding='unicode_escape')
print(df.head())
print(df.columns)
df['InvoiceDate_pdt'] = pd.to_datetime(df['InvoiceDate'])
df_agg = df.groupby(by='CustomerID', as_index=False).agg(count=pd.NamedAgg(column='CustomerID', aggfunc='count'),
                                                         max_purchase_diff_days=pd.NamedAgg(column='InvoiceDate_pdt',
                                                                                            aggfunc=max_days))
df_agg.sort_values('max_purchase_diff_days', ascending=False, inplace=True)
print(df_agg['max_purchase_diff_days'].describe())
df_returning_active = df_agg.query(f'max_purchase_diff_days >=7')
print(df_returning_active.sort_values('max_purchase_diff_days').head())
