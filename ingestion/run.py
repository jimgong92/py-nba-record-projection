from flask import Flask
from server.ingest import ingest

app = Flask(__name__)

ingest()

if (__name__):
  app.run()
  