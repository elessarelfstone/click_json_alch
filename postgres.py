import time

from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, JSON
from sqlalchemy import insert

from data_factory import countries_gen

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/tests')
metadata = MetaData()

json_table = Table('raw_json_test', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('data', JSON))

metadata.create_all(engine)


data_to_insert = [{'data': c} for c in countries_gen('countries.json', size=5000)]

start_time = time.time()

with engine.connect() as conn:
    conn.execute(insert(json_table), data_to_insert)
    conn.commit()

end_time = time.time()
elapsed_time = end_time - start_time

print(f'Execution time: {elapsed_time}')
