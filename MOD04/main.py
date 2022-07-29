from sqlalchemy import create_engine
import pandas as pd


engine = create_engine(
    'postgresql+psycopg2://root:root@localhost/test_db'
)


sql = '''
select * from vw_artist
'''

df = pd.read_sql_query(sql,engine)

df_song = pd.read_sql_query('select * from vw_song',engine)

sql = '''
insert into tb_artist (
SELECT b."date"
	,b."rank"
	,b.artist
	,b.song
FROM PUBLIC."Billboard" b
where b.artist like 'Nirvana'
order by b.artist, b.song, b."date"
);
'''

engine.execute(sql)