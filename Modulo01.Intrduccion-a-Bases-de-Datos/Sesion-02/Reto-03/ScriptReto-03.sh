cd /Users/josecarloscorona/Documents/Github/CursoBD/Intrduccion-a-Bases-de-Datos/Sesion-02/Reto-03
curl -O https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
sed "s/Harris/Ramirez/g" titanic.csv > titanic1.csv
head titanic1.csv
sed "s/0/999/2" titanic.csv > titanic2.csv
head titanic2.csv
sed "s/0/none/g" titanic.csv > titanic3.csv
head titanic3.csv
sed -n "s/William/Brian/p" titanic.csv > titanic4.csv
head titanic4.csv
