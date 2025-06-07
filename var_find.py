def extrair_genotipos(vcf_file, posicoes_alvo):
    """
    Lê um arquivo VCF e retorna dois dicionários:
    - com_mut[pos]: lista de indivíduos com mutação na posição
    - sem_mut[pos]: lista de indivíduos sem mutação (0/0) na posição
    """
    with open(vcf_file, 'r') as vcf:
        # Captura o cabeçalho para obter os nomes dos indivíduos
        for linha in vcf:
            if linha.startswith("#CHROM"):
                cabecalho = linha.strip().split("\t")
                individuos = cabecalho[9:]
                break

        # Dicionários para armazenar os resultados
        com_mut = {pos: [] for pos in posicoes_alvo}
        sem_mut = {pos: [] for pos in posicoes_alvo}

        vcf.seek(0)  # Reinicia a leitura do arquivo

        for linha in vcf:
            if linha.startswith("#"):
                continue
            partes = linha.strip().split("\t")
            pos = partes[1]
            if pos not in posicoes_alvo:
                continue

            genotipos = partes[9:]

            for ind, gt in zip(individuos, genotipos):
                genotype = gt.split(":")[0]
                if genotype == "./.":  # Genótipo ausente: ignora
                    continue
                elif genotype != "0/0":
                    com_mut[pos].append(ind)
                else:
                    sem_mut[pos].append(ind)

    return com_mut, sem_mut


def salvar_resultados(nome_arquivo, dados, titulo):
    """
    Salva os resultados em um arquivo de texto.
    """
    with open(nome_arquivo, 'w') as f:
        for pos, lista_ind in dados.items():
            f.write(f"{titulo} {pos}:\n")
            for ind in lista_ind:
                f.write(f"{ind}\n")
            f.write("\n")


# -----------------------------
# EXEMPLO DE USO
# -----------------------------
if __name__ == "__main__":
    vcf_path = "file.vcf"  # Substitua pelo caminho real
    posicoes = ["827","1095","1189","1243","1555","10398","14484","11778"]  # Substitua pelas posições desejadas

    com, sem = extrair_genotipos(vcf_path, posicoes)

    salvar_resultados("com_mutacao_af_1771.txt", com, "Indivíduos COM mutação na posição")
    salvar_resultados("sem_mutacao_af_1771.txt", sem, "Indivíduos SEM mutação na posição")

