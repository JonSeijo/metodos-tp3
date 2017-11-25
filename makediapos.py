# Jonno

import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--p", help="Abrir pdf en pagina p", default=1, type=int)

args = parser.parse_args()
open_in_page = args.p

informe_name = "diapos"
informe_directorio = "diapos/"

make_pdf_command = "pdflatex " + "-output-directory diapos " + informe_name + ".tex" + " \pdfminorversion=5 \pdfcompresslevel=9 \pdfobjcompresslevel=2"
open_pdf_command = "evince" +  " --page-label=" + str(open_in_page) + " " + informe_directorio + informe_name + ".pdf"

subprocess.call(make_pdf_command.split())
subprocess.call(open_pdf_command.split())