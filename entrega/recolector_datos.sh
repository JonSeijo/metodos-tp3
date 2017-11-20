#!/bin/bash


# Algunos aeropuertos
# LAX: Los Angeles
# MIA: Miami
# MSY: Louis Armstrong New Orleans International Airport
# MCO: Orlando
# DAB: Daytona Beach
# ECP: Panama city


# Algunas aerolineas
# AA: American Airlines
# UA: United Airlines
# WN: SouthWest Airlines
# DL: Delta Airlines
# EV: ExpressJet


# Algunas columnas
# $9: Aerolinea
# $16: Minutos de delay - general
# $17: Aeropuerto de origen
# $22: Cancelado (1 = si)
# $23: Razon cancelacion (B = clima)
# $26: Minutos de delay por clima

outfile="delays_semana_atlanta_deltaairlines.csv"
echo "year,mes,semana,valor" > $outfile

# Ojo que hay datos de cancelaciones por clima solo desde 2003, antes los datos son 0
for year in `seq 2003 2008`; do

	infile="../data/""$year"".csv"

	# Combinar las columas y nombres, algunos ejemplos:

	# cancelados origen miami
	# awk -F, '$17=="MIA" && $22=="1"' $infile > canc_aux.csv

	# Retrasos gral - Origen los angeles - Delta Air Lines
	awk -F, '$17=="LAX" && $9=="DA" && !($16+0<15)' $infile > canc_aux.csv


	# Divide cada mes en cuatro semanas
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

	rm canc_aux.csv
done;

mv $outfile "../experimentos/datos/"$outfile