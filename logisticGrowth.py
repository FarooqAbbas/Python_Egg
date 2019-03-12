import numpy as np
import matplotlib.pyplot as plt
import time
import psycopg2
from pprint import pprint

class DatabaseConnection:
	def __init__(self):
		try:
			self.connection= psycopg2.connect(
			"dbname='emrp2018' user='emrp2018' host='hsrw.space' password='emrp2018!'")
			self.connection.autocommit=True
			self.cursor=self.connection.cursor()
			pprint("connected to database")
		except:
			pprint("Cannot connect to database")

if __name__ == '__main__':
	Database_Connection=DatabaseConnection()
r = .25 # growth rate / yr .25
K = 100 # carrying capacity
t = 40 # number of years
num = np.zeros(t+1)

num[0] = 1
for i in range(t):
    num[i+1] = num[i]+r*num[i]*(1-num[i]/K)
    print('insert',num[i])
    if i<=1:
    	time.sleep(i)
    else:
    	time.sleep(num[i]-num[i-1])

print(num)    
print('insert')
plt.plot(range(t+1),num, 'b')

plt.xlabel('Year')
plt.ylabel('Number')
plt.title('Growth rate: 0.25, Carrying Capacity = 100')
#plt.axvline(np.argmax(np.diff(num)),  color = 'k'  )
plt.show()