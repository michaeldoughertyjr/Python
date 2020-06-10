import pandas as pd

import numpy as np

import datacompy

df1 = pd.read_excel('C:/Users/mdoug016/OneDrive - Ascension/Desktop/Data Resources/Project Data Sets/Trauma Registry/July2019Compare.xlsx', sheet_name = 'Registry')
df2 = pd.read_excel('C:/Users/mdoug016/OneDrive - Ascension/Desktop/Data Resources/Project Data Sets/Trauma Registry/July2019Compare.xlsx', sheet_name = 'EHR')

df2.columns = df1.columns

compare = datacompy.Compare(
    df1,
    df2,
    join_columns='PAT_ACCOUNT',
    abs_tol=0,
    rel_tol=0,
    df1_name='Registry',
    df2_name='Dataset',
    ignore_case = True
)

print(compare.report(sample_count = 1000))

compare.report(sample_count = 1000)