--Create and open db file
.open dbFiles/movie.db

--Create tables
CREATE TABLE CREDITS(
  cast VARCHAR,
  crew VARCHAR,
  id INT,
  PRIMARY KEY (id)
);

CREATE TABLE KEYWORDS(
  id INT,
  keywords VARCHAR,
  PRIMARY KEY (id)
);

CREATE TABLE LINKS_SMALL(
  movieId INT,
  imdbId INT,
  tmdbId INT,
);

CREATE TABLE LINKS(
  movieId INT,
  imdbId INT,
  tmdbId INT,
);

CREATE TABLE MOVIES_METADATA(
  adult VARCHAR,
  belongs_to_collection VARCHAR,
  budget INT,
  genres VARCHAR,
  homepage VARCHAR,
  id INT,
  imdb_id INT,
  original_language VARCHAR,
  original_title VARCHAR,
  overview VARCHAR,
  popularity VARCHAR,
  poster_path VARCHAR,
  production_companies VARCHAR,
  production_countries VARCHAR,
  release_date VARCHAR,
  revenue VARCHAR,
  runtime VARCHAR,
  spoken_languages VARCHAR,
  status VARCHAR,
  tagline VARCHAR,
  title VARCHAR,
  video VARCHAR,
  vote_average VARCHAR,
  vote_count VARCHAR
  PRIMARY KEY (id)
);

CREATE TABLE RATINGS_SMALL(
  userId INT,
  movieId VARCHAR,
  rating DOUBLE,
  timestamp TIMESTAMP,
);

CREATE TABLE RATINGS(
  userId INT,
  movieId VARCHAR,
  rating DOUBLE,
  timestamp TIMESTAMP,
);