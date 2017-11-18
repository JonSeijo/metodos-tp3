#!/bin/bash
# Buscamos numero de vuelos cancelados por mes entre dos aeropuertos. 

# Definimos algunas variables. Ojo que a bash no le gustan los espacios cerca del "=".
# year="2000"
# infile="../data/""$year"".csv"
outfile="canc_por_mes-origen-Detroit-2003-2008.csv"
echo "year,valor" > $outfile
orig_ap="DTW" #DTW Detroit, MCO es Orlando
# dest_ap="ORD"

# La secuencia es:
# 1. Primero filtramos por vuelos cancelados. Esto lo hacemos una unica vez y lo guardamos en el archivo canc_aux.csv
# 2. Del output de 1, filtramos las lineas que matchean el mes. Esto es facil de hacer con el comando grep.
# 3. Contamos la cantidad de lineas con el comando wc.
# El resultado queda en $outfile, es un vector con las cancelaciones por mes del año elegido.
for year in `seq 2003 2008`; do
	
	infile="../data/""$year"".csv"

	awk -F, '$17 == "'"$orig_ap"'" && $22=="1"' $infile > canc_aux.csv

	for mes in `seq 1 12`; do cat canc_aux.csv | grep $year,$mes | echo $year","`wc -l` >> $outfile; done;

done;

mv "canc_por_mes-origen-Detroit-2003-2008.csv" "../experimentos/datos/"

# Borramos el archivo auxiliar.
rm canc_aux.csv
