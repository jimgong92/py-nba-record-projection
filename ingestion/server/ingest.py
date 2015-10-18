from .sources.bref import ingest_players
from .sources.bref import ingest_win_shares
from .sources.espn import ingest_rpm

def ingest():
  ingest_players()
  ingest_win_shares()
  ingest_rpm()
