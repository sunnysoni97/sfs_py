import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data_sets/Irregularity_score.csv')

x = data['Sleep_frac'].values.reshape(-1,1)
y = data['Irr_score'].values.reshape(-1,1)

reg = LinearRegression()
reg.fit(x,y)

pred = reg.predict(x)

plt.figure(figsize=(16, 8))
plt.scatter(
    data['Sleep_frac'],
    data['Irr_score'],
    c='black'
)
plt.plot(
    data['Sleep_frac'],
    pred,
    c='blue',
    linewidth=2
)
plt.xlabel("Sleep Fraction (Sleep in a day/ Optimal Sleep)")
plt.ylabel("Irregularity Score")
plt.show()