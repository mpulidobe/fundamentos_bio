def fasta_to_tsv(fasta_path: str, tsv_output: str) -> None:
    """
    Convierte un archivo FASTA a formato TSV.
    
    Parámetros:
        fasta_path (str): Ruta del archivo FASTA de entrada.
        tsv_output (str): Nombre del archivo TSV de salida.
    """
    with open(fasta_path, "r") as fasta, open(tsv_output, "w") as tsv:
        # Escribir encabezado
        tsv.write("id\tdescripcion\tsecuencia\n")
        
        seq_id, desc, seq = None, None, []

        for line in fasta:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                # Si ya había una secuencia previa, escribirla
                if seq_id is not None:
                    tsv.write(f"{seq_id}\t{desc}\t{''.join(seq)}\n")
                # Nuevo encabezado FASTA
                parts = line[1:].split(maxsplit=1)
                seq_id = parts[0]
                desc = parts[1] if len(parts) > 1 else ""
                seq = []
            else:
                seq.append(line)
        
        # Escribir la última secuencia
        if seq_id is not None:
            tsv.write(f"{seq_id}\t{desc}\t{''.join(seq)}\n")


fasta_to_tsv("fundamentos_bio/entrega_1/ncbi_dataset/ncbi_dataset/data/GCA_002853715.1/GCA_002853715.1_ASM285371v1_genomic.fna", "Escherichia_coli_strain_14EC020.tsv")
