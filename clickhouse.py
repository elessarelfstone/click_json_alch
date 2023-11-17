import json
from sqlalchemy import create_engine, MetaData, Table, Column, String, JSON
from sqlalchemy import insert

from data_factory import countries_gen

engine = create_engine('clickhouse+native://default:@localhost/default')
metadata = MetaData()

json_table = Table('raw_json_test', metadata,
                   Column('data', String))

metadata.create_all(engine)


data_to_insert = [{'data': json.dumps(c)} for c in countries_gen('countries.json', size=500000)]
# print(data_to_insert)

with engine.connect() as conn:
    conn.execute(insert(json_table), data_to_insert)
    conn.commit()
