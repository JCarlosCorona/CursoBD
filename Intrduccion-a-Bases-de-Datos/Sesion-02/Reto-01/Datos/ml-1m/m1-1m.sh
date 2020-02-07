sed "s/::/,/g" movies.dat > movies.csv
ls
echo "Movie ID,Title,Genres" | cat - movies.csv > movies-h.csv
head -n 20 movies-h.csv
sed "s/::/,/g" ratings.dat > ratings.csv
ls
echo "User ID,Movie ID,Rating,Timestamp" | cat - ratings.csv > ratings-h.csv
head -n 20 ratings-h.csv
