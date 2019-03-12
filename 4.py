from sqlalchemy import create_engine
engine=create_engine("postgresql://emrp2018:emrp2018!@hsrw.space/emrp2018")
result_set=engine.execute('Select * from public."TTNGateway"')
for r in result_set:
	print(r)