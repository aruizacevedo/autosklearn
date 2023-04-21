
import autosklearn

import pandas as pd

df = pd.read_csv('housing.csv')

df.head()

df.dtypes


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
