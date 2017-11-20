#!/bin/bash

# Esta pensado para cancelaciones pero es re facil cambiar por otra cosa,
# ver los numeros de columnas en la pagina


# MIA: Miami
# MSY: Louis Armstrong New Orleans International Airport
# MCO: Orlando
# DAB: Daytona Beach
# ECP: Panama city

outfile="delays_semana_atlanta_americanairlines.csv"
echo "year,mes,semana,valor" > $outfile

# Hay datos de cancelaciones por clima solo desde 2003, antes los datos son 0
for year in `seq 2003 2008`; do

	infile="../data/""$year"".csv"

	# SOLO DESCOMENTAR UNO



	# Retrasos gral - Origen los angeles - United Air Lines
	# awk -F, '$17=="LAX" && $9=="UA" && !($16+0<15)' $infile > canc_aux.csv

	# Retrasos gral - Origen los angeles - SouthWest Airlines
	# awk -F, '$17=="LAX" && $9=="WN" && !($16+0<15)' $infile > canc_aux.csv



	# Retrasos gral - Origen Atlanta - United Air Lines
	# awk -F, '$17=="ATL" && $9=="UA" && !($16+0<15)' $infile > canc_aux.csv

	# Retrasos gral - Origen Atlanta - SouthWest Airlines
	# awk -F, '$17=="ATL" && $9=="WN" && !($16+0<15)' $infile > canc_aux.csv

	# Retrasos gral - Origen Atlanta - DeltaAirLines
	# awk -F, '$17=="ATL" && $9=="DL" && !($16+0<15)' $infile > canc_aux.csv

	# Retrasos gral - Origen Atlanta - American Airlines
	awk -F, '$17=="ATL" && $9=="AA" && !($16+0<15)' $infile > canc_aux.csv




	# con WeatherDelay origen miami
	# awk -F, '$17=="MIA" && !($26+0<15) && !($26=="NA")' $infile > canc_aux.csv

	# cancelados general
	# awk -F, '$22=="1"' $infile > canc_aux.csv

	# cancelados origen miami
	# awk -F, '$17=="MIA" && $22=="1"' $infile > canc_aux.csv

	# cancelados origen atlanta
	# awk -F, '$17=="ATL" && $22=="1"' $infile > canc_aux.csv

	# cancelados origen los angeles
	# awk -F, '$17=="LAX" && $22=="1"' $infile > canc_aux.csv

	# cancelados por clima origen los angeles
	# awk -F, '$17=="LAX" && $22=="1" && $23=="B"' $infile > canc_aux.csv

	# cancelados por clima origen orlando
	# awk -F, '$17=="MCO" && $22=="1" && $23=="B"' $infile > canc_aux.csv

	# cancelados por clima origen miami
	# awk -F, '$17=="MIA" && $22=="1" && $23=="B"' $infile > canc_aux.csv

	# cancelados por clima
	# awk -F, '$22=="1" && $23=="B"' $infile > canc_aux.csv




	# Cancelados gral - Delta Air Lines
	# awk -F, '$9=="DL" && $22=="1"' $infile > canc_aux.csv

	# Cancelados gral - United Air Lines
	# awk -F, '$9=="UA" && $22=="1"' $infile > canc_aux.csv




	# Retrasos por clima - United Airlines
	# awk -F, '$9=="UA"  && !($26=="NA") && !($26+0<15)' $infile > canc_aux.csv

	# cancelados por clima American Airlines
	# awk -F, '$9=="AA" && $22=="1" && $23=="B"' $infile > canc_aux.csv

	# Retrasos por clima - American Airlines
	# awk -F, '$9=="AA"  && !($26=="NA") && !($26+0<15)' $infile > canc_aux.csv

	# cancelados por clima ExpressJet
	# awk -F, '$9=="EV" && $22=="1" && $23=="B"' $infile > canc_aux.csv






	# cancelados general - American Airlines
	# awk -F, '$9=="AA" && $22=="1"' $infile > canc_aux.csv

	# cancelados general - ExpressJet
	# awk -F, '$9=="EV" && $22=="1"' $infile > canc_aux.csv




	# Retrasos - ExpressJet
	# awk -F, '$9=="EV"  && !($15+$16+0<15)' $infile > canc_aux.csv


	for mes in `seq 1 12`; do
		cat canc_aux.csv | grep -E $year,$mes',[1-7],' | echo $year","$mes",1,"`wc -l` >> $outfile;
		cat canc_aux.csv | grep -E $year,$mes,'([8-9]|1[0-5]),' | echo $year","$mes",2,"`wc -l` >> $outfile;
		cat canc_aux.csv | grep -E $year,$mes,'(1[6-9]|2[0-3]),' | echo $year","$mes",3,"`wc -l` >> $outfile;
		cat canc_aux.csv | grep -E $year,$mes,'(2[4-9]|3[01]),' | echo $year","$mes",4,"`wc -l` >> $outfile;
	done;


	# SUMA DE DELAYS SEMANA A SEMANA
	# for mes in `seq 1 12`; do
	# 	cat canc_aux.csv | grep -E $year,$mes',[1-7],' > suma_aux.csv;
	# 	echo $year","$mes",1,"`awk -F, '{sum += $26} END {print sum}' suma_aux.csv` >> $outfile

	# 	cat canc_aux.csv | grep -E $year,$mes,'([8-9]|1[0-5]),' > suma_aux.csv;
	# 	echo $year","$mes",2,"`awk -F, '{sum += $26} END {print sum}' suma_aux.csv` >> $outfile

	# 	cat canc_aux.csv | grep -E $year,$mes,'(1[6-9]|2[0-3]),' > suma_aux.csv;
	# 	echo $year","$mes",3,"`awk -F, '{sum += $26} END {print sum}' suma_aux.csv` >> $outfile

	# 	cat canc_aux.csv | grep -E $year,$mes,'(2[4-9]|3[01]),' > suma_aux.csv;
	# 	echo $year","$mes",4,"`awk -F, '{sum += $26} END {print sum}' suma_aux.csv` >> $outfile
	# done;

	# rm canc_aux.csv
done;

mv $outfile "../experimentos/datos/"$outfile