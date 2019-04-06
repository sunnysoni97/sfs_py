import matplotlib.pyplot as plt
import pandas as pd


def suggest_temp(cur_rad):
	plt.plot(201,cur_rad,'ro',c='orange')
	if(cur_rad>0 and cur_rad<2.5):
		plt.text(100,23,str("Optimal Radiation Conditions!"), horizontalalignment="center", verticalalignment="center")
	else:
		plt.text(100,23,str("{0:.2f}".format(cur_rad-2.5))+(" deviated from optimal"), horizontalalignment="center", verticalalignment="center")

def avg(data):
	sum = 0
	count = 0
	for i in data['Exposure']:
		sum +=i
		count +=1
	avg_r = sum/count
	return avg_r


cur_rad = float(input("Current radiation value : "))
data = pd.read_csv('data_sets/radiation_data2.csv')

plt.plot(
	data['S.no'],
	data['Exposure'],
	c='blue')
plt.xlabel("Radiation Instances")
plt.ylabel("Radiation Value (in mG)")
plt.legend()
(avg_r)=avg(data)
suggest_temp(cur_rad)
plt.text(100,25,str("Average Radiation Value: "+ str(avg_r)), horizontalalignment="center", verticalalignment="center")
plt.show()