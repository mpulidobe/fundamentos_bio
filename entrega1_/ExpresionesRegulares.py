import re

with open ("fundamentos_bio/entrega1_/Escherichia_coli_gca_006351485.ASM635148v1.pep.all.fa") as file:

    '''Funcion re.match
        Revisa si el texto comienza con el patron especificado'''

    for line in file:
        if re.match(r"^>ENSB", line):
            print("Cabecera encontrada:", line.strip())
