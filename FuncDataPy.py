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

	def insertTTNGateway(self):
		new_record=("18","eui-","7837377","1","-75","6","70.1","6.5485168","51.3527573","16-05-2011")
		#insert_command="INSERT INTO public."Bin"(GatewayId,gtw_id,timestamp,channel,rssi,snr,altitude,longitude,latitude,time) VALUES ('"+new_record[0]+"','"+new_record[1]+"','"+new_record[2]+"','" + new_record[3] + "','"+new_record[4]+"','" + new_record[5] + "','"+new_record[6]+"','" + new_record[7] + "','" + new_record[8] + "','" + new_record[9]+"')"
		insert_command="INSERT INTO public."Bin"(GatewayId,gtw_id,timestamp,channel,rssi,snr,altitude,longitude,latitude,time) VALUES ('"+new_record[0]+"','"+new_record[1]+"','"+new_record[2]+"','" + new_record[3] + "','"+new_record[4]+"','" + new_record[5] + "','"+new_record[6]+"','" + new_record[7] + "','" + new_record[8] + "','" + new_record[9]+"')"
		
		pprint(insert_command)
		self.cursor.execute(insert_command)
if __name__ == '__main__':
	Database_Connection=DatabaseConnection()
	Database_Connection.insertTTNGateway()		