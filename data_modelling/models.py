import numpy as np
import pandas as pd
import matplotlib.pylab as plt
#import scipy.stats as stats



df = pd.read_csv('nba_stats3.csv')
df.columns = df.iloc[0]
df2 = df.drop_duplicates(subset=df.iloc[2], keep='first')
print(df2.head())