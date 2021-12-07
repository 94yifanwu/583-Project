# Remove previously initialized database file
rm ./dbFiles/movie.db

# Create schema
sqlite3 < ./bin/dbInit.sql

# Add rows
sqlite-utils insert ./dbFiles/movie.db CREDITS --csv ./csvFiles/credits.csv
sqlite-utils insert ./dbFiles/movie.db KEYWORDS --csv ./csvFiles/keywords.csv
sqlite-utils insert ./dbFiles/movie.db LINKS_SMALL --csv ./csvFiles/links_small.csv
sqlite-utils insert ./dbFiles/movie.db LINKS --csv ./csvFiles/links.csv
sqlite-utils insert ./dbFiles/movie.db MOVIES_METADATA --csv ./csvFiles/movies_metadata.csv
sqlite-utils insert ./dbFiles/movie.db RATINGS_SMALL --csv ./csvFiles/ratings_small.csv
sqlite-utils insert ./dbFiles/movie.db RATINGS --csv ./csvFiles/ratings.csv
