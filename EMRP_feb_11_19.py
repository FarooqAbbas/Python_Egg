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
		postgres_insert_query = """ INSERT INTO public."SensorData" ("DeviceId","Level","Battery",app_id,dev_id,hardware_serial,
        port,cunter,payload_raw,"time",frequency,modulation,data_rate,airtime,coding_rate,"TTNGatewayId",payload_fields)
         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

		record_to_insert = ("12","23","12",application_id,device,hardware_serial_number,port_number,counter,payload_raw,time,
        frequency_value,modulation_value,data_rate_value,airtime_value,coding_rate_value,fetched_gateway,str(payload_fields))
		self.cursor.execute(postgres_insert_query, record_to_insert)
        #self.connection.commit()

if __name__ == '__main__':
	Database_Connection=DatabaseConnection()
	Database_Connection.insertTTNGateway()        