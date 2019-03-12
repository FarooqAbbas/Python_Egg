import psycopg2
import calendar;
import time;
import datetime
import random


gatewayId=1
gtw_Id="eui-b827ghkl"
timestamp1 = calendar.timegm(time.gmtime())

now = datetime.datetime.now()
time1=now.isoformat()

channel=list(range(0,9))
rssi=list(range(-75,-80))

try:
    conn = psycopg2.connect("dbname='emrp2018' user='emrp2018' host='hsrw.space' password='emrp2018!'")
except:
    print ("I am unable to connect to the database")

cur=conn.cursor()
#the way to insert the data into table.
#cur.execute('INSERT INTO public."Bin" ("Id","LocationId","DeviceId") VALUES(1,2,123)')
#cur.execute('INSERT INTO public."TTNGateway"("GatewayId","gtw_id","timestamp","time","channel","rssi","snr","altitude","longitude","latitude") VALUES(gatewayId,gtw_id,timestamp1,time1,channel,rssi,6,70.1,6.5485168,51.3527573)')
#cur.execute('INSERT INTO public."TTNGateway" VALUES(4,827,12345,-75,6,70.1,6.5485168,51.3527573,16-05-2011)')

cur.execute(""" INSERT INTO public."TTNGateway" (GatewayId, gtw_id,timestamp,channel,rssi,"snr","altitude","longitude","latitude","time") VALUES (%(int)s, %(str)s, %(int)s, %(int)s, %(long)s,); """, {'int': 5, 'str': "eui-b827", 'date': datetime.date(2005, 11, 18)})
#cur.execute('select * from public."Bin" where "LocationId" >2')
conn.commit()