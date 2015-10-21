CREATE TABLE player (
  player_id UUID PRIMARY KEY,
  player_name VARCHAR(255),
  player_position VARCHAR(50),
  player_age SMALLINT,
  current_team VARCHAR(50),
  percent_playing_time NUMERIC(4,4),
  rpm NUMERIC(4,4),
  win_shares NUMERIC(4,4)
);
