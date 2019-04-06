import matplotlib.pyplot as plt
import pandas as pd


def suggest_temp(cur_temp):
	plt.plot(151,cur_temp,'ro',c='orange')
	if(cur_temp>50):
		if(cur_temp>70 and cur_temp<73):
			plt.text(50,35,str("Optimal Temperature Conditions!"), horizontalalignment="center", verticalalignment="center")
		else:
			plt.text(50,35,str("{0:.2f}".format(cur_temp-71.6))+(" deviated from optimal"), horizontalalignment="center", verticalalignment="center")
	else:
		if(cur_temp>20.5 and cur_temp<23.5):
			plt.text(50,35,str("Optimal Temperature Conditions!"), horizontalalignment="center", verticalalignment="center")
		else:
			plt.text(50,35,str("{0:.2f}".format(cur_temp-22))+(" deviated from optimal"), horizontalalignment="center", verticalalignment="center")
def avg(data):
	sum = 0
	sum2 = 0
	count = 0
	for i in data['current_temp_c']:
		sum +=i
		count +=1
	for i in data['current_temp_f']:
		sum2+=i

	avg_c = sum/count
	avg_f = sum2/count
	return (avg_c, avg_f)


cur_temp = float(input("Current room temp : "))
data = pd.read_csv('data_sets/temp_march.csv')

plt.plot(
	data['S.No.'],
	data['current_temp_c'],
	c='blue')
plt.plot(
	data['S.No.'],
	data['current_temp_f'],
	c='black')
plt.xlabel("Temperature Instances")
plt.ylabel("Temperature(*C,*F)")
plt.legend()
(avg_c, avg_f)=avg(data)
suggest_temp(cur_temp)
plt.text(50,50,str("Average Temp: "), horizontalalignment="center", verticalalignment="center")
plt.text(50,45,str("Celsius: "+ str(avg_c)), horizontalalignment="center", verticalalignment="center")
plt.text(50,40,str("Fahranheit: "+str(avg_f)), horizontalalignment="center", verticalalignment="center")
plt.show()