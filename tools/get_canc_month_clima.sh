#!/bin/bash
# Buscamos numero de vuelos cancelados por mes entre dos aeropuertos.

# MIA: Miami
# MSY: Louis Armstrong New Orleans International Airport
# MCO: Orlando
# DAB: Daytona Beach
# ECP: Panama city


outfile="cancelaciones_mes_clima.csv"
echo "Year,Month,WeatherDelay" > $outfile

for year in `seq 2000 2008`; do
# for year in `seq 2007 2008`; do

	infile="../data/""$year"".csv"

	# con WeatherDelay
	awk -F, '!($26=="0") && !($26=="NA")' $infile > canc_aux.csv

	# cancelados
	# awk -F, '$22=="1"' $infile > canc_aux.csv

	# cancelados por clima
	# awk -F, '$22=="1" && $23=="B"' $infile > canc_aux.csv

	# cancelados por clima hacia destino X ($18 == .. )
	# awk -F, '($18=="MSY" || $18=="MIA" || $18=="MCO") && $22=="1" && $23=="B"' $infile > canc_aux.csv

	for i in `seq 1 12`; do
		cat canc_aux.csv | grep $year,$i | echo $year","$i,`wc -l`
	done >> $outfile;

	rm canc_aux.csv

done