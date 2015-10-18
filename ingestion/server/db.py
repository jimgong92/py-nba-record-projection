import psycopg2
import os

conn = psycopg2.connect(
  dbname='nba_proj',
  database='nba_proj',
  user='postgres',
  password='postgres',
  host='http://localhost',
  port=5432
)
