import re

with open ("fundamentos_bio/entrega1_/Escherichia_coli_gca_006351485.ASM635148v1.pep.all.fa") as file:

    '''Funcion re.match
        Revisa si el texto comienza con el patron especificado'''

    for line in file:
        if re.match(r"^>ENSB", line):
            print("Cabecera encontrada:", line.strip())

    '''Funcion re.findall
    Busca todas las coincidencias dentro de cada línea del archivo
    '''
    for line in file:
        if line.startswith(">"):  # Solo analizamos las cabeceras
            matches = re.findall(r"(ENSB\w+)", line)  
            if matches:
                print("Identificadores encontrados:", matches)
