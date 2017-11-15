#!/bin/bash

# Esta pensado para cancelaciones pero es re facil cambiar por otra cosa,
# ver los numeros de columnas en la pagina


# MIA: Miami
# MSY: Louis Armstrong New Orleans International Airport
# MCO: Orlando
# DAB: Daytona Beach
# ECP: Panama city


outfile="delay_clima_origen_miami.csv"
echo "year,mes,semana,valor" > $outfile

# Hay datos de cancelaciones por clima solo desde 2003, antes los datos son 0
for year in `seq 2003 2008`; do

	infile="../data/""$year"".csv"

	# SOLO DESCOMENTAR UNO

	# con WeatherDelay origen miami
	awk -F, '$17=="MIA" && !($26+0<15) && !($26=="NA")' $infile > canc_aux.csv

	# cancelados
	# awk -F, '$22=="1"' $infile > canc_aux.csv

	# cancelados destino miami
	# awk -F, '$18=="MIA" && $22=="1"' $infile > canc_aux.csv

	# cancelados origen miami
	# awk -F, '$17=="MIA" && $22=="1"' $infile > canc_aux.csv

	# cancelados por clima destino miami
	# awk -F, '$18=="MIA" && $22=="1" && $23=="B"' $infile > canc_aux.csv

	# cancelados por clima origen miami
	# awk -F, '$17=="MIA" && $22=="1" && $23=="B"' $infile > canc_aux.csv

	# cancelados destino atlanta
	# awk -F, '$18=="ATL" && $22=="1"' $infile > canc_aux.csv

	# cancelados por clima destino atlanta
	# awk -F, '$18=="ATL" && $22=="1" && $23=="B"' $infile > canc_aux.csv


	# cancelados por clima
	# awk -F, '$22=="1" && $23=="B"' $infile > canc_aux.csv

	# cancelados por clima hacia destino X ($18 == .. ), pueden agregarse mas destinos
	# awk -F, '($18=="MSY" || $18=="MIA" || $18=="MCO") && $22=="1" && $23=="B"' $infile > canc_aux.csv
	# awk -F, '($18=="MIA") && $22=="1" && $23=="B"' $infile > canc_aux.csv

	# Guardo valores semana a semana,
	for mes in `seq 1 12`; do
		cat canc_aux.csv | grep -E $year,$mes',[1-7],' | echo $year","$mes",1,"`wc -l` >> $outfile;
		cat canc_aux.csv | grep -E $year,$mes,'([8-9]|1[0-5]),' | echo $year","$mes",2,"`wc -l` >> $outfile;
		cat canc_aux.csv | grep -E $year,$mes,'(1[6-9]|2[0-3]),' | echo $year","$mes",3,"`wc -l` >> $outfile;
		cat canc_aux.csv | grep -E $year,$mes,'(2[4-9]|3[01]),' | echo $year","$mes",4,"`wc -l` >> $outfile;
	done;

	# rm canc_aux.csv

done;