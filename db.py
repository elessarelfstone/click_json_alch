from sqlalchemy import create_engine, MetaData, Table, Column, String, JSON
from sqlalchemy import insert

engine = create_engine('clickhouse+native://default:@localhost/default')
metadata = MetaData()

json_table = Table('raw_json_test', metadata,
                   Column('data', String))

metadata.create_all(engine)

data_to_insert = [
    # {'data': '{"name": "Rob", "age": 31, "attrs": [{"sex": "male"}]}'},
    # {'data': '{"name": "Jane", "age": 23, "attrs": [{"sex": "female"}]}'},
    {'data': '{"name": "Bruce", "age": 29, "attrs": "just_string"}'}
    # {'data': '{"name": "Rob", "age": 31}'},
    # {'data': '{"name": "Jane", "age": 23}'}
]

with engine.connect() as conn:
    conn.execute(insert(json_table), data_to_insert)
