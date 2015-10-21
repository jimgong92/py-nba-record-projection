# Base data source contains player information

import psycopg2
import uuid
from csv import DictReader, register_dialect
from io import BytesIO, TextIOWrapper
from ..db import conn

PLAYER_DATA_FILE = 

def insert_player(d):
  c = (
    "player_id",
    "player_name",
    "player_team",
    "percent_playing_time"
  )
  cur = conn.cursor()
  # try:
  #   cur.execute("INSERT INTO player ("
  #               ""
  #               " VALUES ())"
  # finally:
  #   conn.commit()
  #   cur.close()

def ingest_players():
  print('INGESTING WIN SHARES FROM BASKETBALL_REFERENCE')
