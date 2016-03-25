import psycopg2
import os


conn = psycopg2.connect(
  dbname='nba_record_proj',
  database='nba_record_proj',
  user='postgres',
  password='',
  host='localhost',
  port=5432
)

# Initialize database

def rebuild_db():
  c = conn.cursor()
  c.execute('DROP TABLE IF EXISTS player')
  c.execute('CREATE TABLE player ('
            'player_id UUID PRIMARY KEY,'
            'player_name VARCHAR(255),'
            'player_position VARCHAR(50),'
            'player_age SMALLINT,'
            'current_team VARCHAR(50),'
            'percent_playing_time NUMERIC(4,4),'
            'rpm NUMERIC(4,4),'
            'win_shares NUMERIC(4,4)'
            ')')

rebuild_db()
