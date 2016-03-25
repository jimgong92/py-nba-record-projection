# Base data source contains player information

import psycopg2
import uuid
import requests
from csv import DictReader, register_dialect
from io import BytesIO, TextIOWrapper
from zipfile import ZipFile
from ..db import conn

PLAYER_DATA_URL = 'https://github.com/jimgong92/py-nba-record-projection/blob/master/ingestion/data/player_minutes_1516.csv.zip?raw=true' 
PLAYER_DATA_FILE = 'player_minutes_1516.csv'

def insert_player(d):
  c = (
    'Player',
    'Team',
    'Percent Playing Time'
  )
  cur = conn.cursor()
  try:
    cur.execute('INSERT INTO player ('
                'player_id, player_name, current_team, percent_playing_time'
                ') VALUES (%s, %s, %s, %s)', (
                  str(uuid.uuid4()), d[c[0]], d[c[1]], d[c[2]]
                ))
  finally:
    conn.commit()
    cur.close()

def ingest_players():
  request = requests.get(PLAYER_DATA_URL)
  with ZipFile(BytesIO(request.content), 'r') as zip_file:
    with zip_file.open(PLAYER_DATA_FILE) as player_file:
      stream = TextIOWrapper(player_file)
      csv = DictReader(stream, delimiter=',')
      try:
        print('INGESTION: PLAYER INFO FROM %s' % PLAYER_DATA_FILE)
        for row in csv:
          insert_player(row)
        print('INGESTION: PLAYER INFO - COMPLETE')
      except Exception as e:
        print('ERROR: %s' % e)

