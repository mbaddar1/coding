import pandas as pd
# Quesion # 1 https://www.kdnuggets.com/2022/04/15-python-coding-interview-questions-must-know-data-science.html
if __name__ == '__main__':
    df = pd.read_csv('./employees.csv')
    print(df.head())
    merged_df = pd.merge(left=df, right=df, how='cross')  # no on param , doesn't make sense
    # https://stackoverflow.com/questions/69532422/mergeerror-can-not-pass-on-right-on-left-on-or-set-right-index-true-or-left-i
    print(merged_df.columns)
    merged_df['salary_diff'] = abs(merged_df['SALARY_x']-merged_df['SALARY_y'])
    print(merged_df['salary_diff'].describe())
    print(max(merged_df['salary_diff']))