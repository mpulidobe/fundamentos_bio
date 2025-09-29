def fasta_to_tsv(fasta_path: str, tsv_output: str) -> None:
    with open(fasta_path, "r") as fasta, open(tsv_output, "w") as tsv:
        tsv.write("id\tdescription\tsequence\n")
        
        id, description, sequence = None, None, []

        for line in fasta:
            line = line.strip()
            if line.startswith(">"):
                if id is not None:
                    tsv.write(f"{id}\t{description}\t{''.join(sequence)}\n")
                # Reiniciar variables
                parts = line[1:].split(maxsplit=1)
                id = parts[0]
                description = parts[1] if len(parts) > 1 else ""
                sequence = []
            else:
                sequence.append(line)

        # Guardar el último registro
        if id:
            tsv.write(f"{id}\t{description}\t{''.join(sequence)}\n")

fasta_to_tsv("fundamentos_bio/entrega1_/Escherichia_coli_gca_006351485.ASM635148v1.pep.all.fa", "Escherichia_coli_proteins.tsv")
