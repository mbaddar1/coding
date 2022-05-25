"""
https://platform.stratascratch.com/coding/10172-best-selling-item?code_type=2
"""
from typing import Iterable

import numpy as np
import pandas as pd


def max_selling(x: Iterable[tuple]) -> str:
    id_, selling = zip(*x)
    idx_max = np.argmax(selling)
    id_max = id_[idx_max]
    return id_max


if __name__ == '__main__':
    df = pd.read_csv("customer_purchase_data.csv", sep=',', encoding='unicode_escape')
    print(df.columns)
    print(df.describe())

    df['InvoiceDate_pdt'] = pd.to_datetime(df['InvoiceDate'])
    df['MY'] = df['InvoiceDate_pdt'].dt.to_period('M')
    df['total'] = np.multiply(df['Quantity'], df['UnitPrice'])
    df_agg = df.groupby(by=['StockCode', 'MY'], as_index=False).agg(
        tot_selling=pd.NamedAgg(column='total', aggfunc='sum'))
    df_agg['StockCode_tot_selling'] = list(zip(df_agg['StockCode'], df_agg['tot_selling']))
    print(df_agg.head())
    df_agg2 = df_agg.groupby(by='MY', as_index=False).agg(
        id_max_sell=pd.NamedAgg(column='StockCode_tot_selling', aggfunc=max_selling))
    print(df_agg2.head(20))
