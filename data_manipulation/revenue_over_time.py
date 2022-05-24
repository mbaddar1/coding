"""
https://platform.stratascratch.com/coding/10314-revenue-over-time?code_type=2
"""
import pandas as pd

if __name__ == '__main__':
    pass
df = pd.read_csv('./uk_retailer_data.csv', sep=',', encoding='unicode_escape')
df['InvoiceDateTime_pd'] = pd.to_datetime(df['InvoiceDate'])
df['InvoiceDateTime_Month_Year'] = df['InvoiceDateTime_pd'].apply(lambda x: pd.to_datetime(f'{x.year}-{x.month}-01'))
# df.to_csv('./tmp2.csv', index=False, sep=',')
df['tot_revenue'] = df['Quantity'] * df['UnitPrice']

df_agg1 = df.groupby(by=['CustomerID', 'InvoiceDateTime_Month_Year'], as_index=False).agg(
    agg_revenue=pd.NamedAgg(column='tot_revenue', aggfunc='sum')).sort_values(
    by=['CustomerID', 'InvoiceDateTime_Month_Year'])
df_agg1.to_csv('./tmp2.csv', index=False, sep=',')
# TODO
# 1) make aux table with customer id and months from jan - min_year to dec - max_year
# 2) Join to fill time gaps
# 3) fill nan avg revenue with zero
# 4) add agg function that sorts by time and run rolling average
