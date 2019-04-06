import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
import numpy as np

def predict_condition(data, model):
	ans = model.predict(np.reshape([[data]],(-1,1)))
	plt.plot(data,ans[0],'ro',c='red')
	if(ans[0]==1):
		plt.text(350,1.5,str("Baby maybe hungry!"), horizontalalignment="center", verticalalignment="center") 		
	elif(ans[0]==2):
		plt.text(350,1.5,str("Baby maybe tired!"), horizontalalignment="center", verticalalignment="center") 		
	elif(ans[0]==3):
		plt.text(350,1.5,str("Baby maybe unwell!"), horizontalalignment="center", verticalalignment="center") 		
	else:
		plt.text(350,1.5,str("Baby may have colic!"), horizontalalignment="center", verticalalignment="center") 		

data = pd.read_csv('data_sets/Cry_data.csv')

x = data['Freq'].values.reshape(-1,1)
y = data['Emotion'].values.reshape(-1,1)

reg = LogisticRegression(solver = 'lbfgs')
reg.fit(x,y)

pred = reg.predict(x)

new_data = int(input("Frequency of noise : "))

plt.figure(figsize=(16, 8))
"""plt.scatter(
    data['Freq'],
    data['Emotion'],
    c = 'black'
)"""

plt.scatter(
	data['Freq'],
	pred,
	c='blue',
)

plt.xlabel("Frequencies of Crying")
plt.ylabel("Emotion")
plt.text(100,4,str("'1' : Hungry"), horizontalalignment="center", verticalalignment="center")
plt.text(100,3.5,str("'2' : Tired"), horizontalalignment="center", verticalalignment="center")
plt.text(100,3,str("'3' : Unwell"), horizontalalignment="center", verticalalignment="center")
plt.text(100,2.5,str("'4' : Colic"), horizontalalignment="center", verticalalignment="center")
predict_condition(new_data,reg)
plt.show()