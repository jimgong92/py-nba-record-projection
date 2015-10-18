CREATE TABLE player (
  id VARCHAR(255) PRIMARY KEY,
  position VARCHAR(50),
  age SMALLINT,
  current_team VARCHAR(50),
  o_rpm NUMERIC(4,4),
  d_rpm NUMERIC(4,4),
  o_ws NUMERIC(4,4),
  d_ws NUMERIC(4,4)
);
