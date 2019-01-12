import psycopg2
try:
    conn = psycopg2.connect("dbname='emrp2018' user='emrp2018' host='hsrw.space' password='emrp2018!'")
except:
    print ("I am unable to connect to the database")

cur=conn.cursor()
#the way to insert the data into table.
#cur.execute('INSERT INTO public."Bin" ("Id","LocationId","DeviceId") VALUES(1,2,123)')
cur.execute('INSERT INTO public."Location" ("Id","Latitude","Longitude") VALUES(1,2,123)')
#cur.execute('select * from public."Bin" where "LocationId" >2')
conn.commit()