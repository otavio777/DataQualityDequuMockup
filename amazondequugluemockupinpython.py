# -*- coding: utf-8 -*-
"""AmazonDequuGlueMockupInPython.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ti6g9Xul0kBz5hbT7HWG9kdAiB3G9wd2

# Amazon Dequu + Glue Mockup
"""

import pandas as pd

### reference: https://www.data.gouv.fr/en/datasets/all-datasets/#_

df = pd.read_excel('/content/drive/MyDrive/CS/all-datasets.xlsx')

df.head()

df.columns

"""## Statistics"""

df[['x', 'y']].describe()

"""## Completeness"""

def check_dataframe_completeness(dataframe):
  for column in dataframe:
    s = df[column]
    print(column, 'has', s.isna().sum(), 'empty cells.')

check_dataframe_completeness(df)

"""## Format Consistency"""

!pip install validators

import validators

def check_uuid_consistency(serie):

  count_invalid_entries = 0

  for row in serie:
    test = validators.uuid(row)
    if not test:
      print('Entry', row, ' is not valid.')

check_uuid_consistency(df.dataset_id)