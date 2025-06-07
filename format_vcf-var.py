def process_vcf(input_vcf_path, output_txt_path):
    """
    Processa um arquivo VCF, extrai informações de variantes e as anota em um novo arquivo.

    Args:
        input_vcf_path (str): Caminho para o arquivo VCF de entrada.
        output_txt_path (str): Caminho para o arquivo de texto de saída.
    """
    with open(input_vcf_path, 'r') as infile, open(output_txt_path, 'w') as outfile:
        for line in infile:
            if line.startswith('#'):  # Ignora linhas de cabeçalho
                continue
            
            parts = line.strip().split('\t')
            if len(parts) < 5:  # Garante que a linha tem colunas suficientes para uma variante
                continue

            chrom = parts[0]
            pos = int(parts[1])
            ref = parts[3]
            alt = parts[4]

            # Assume que a primeira alternativa é a relevante se houver múltiplas
            # Se precisar de um tratamento diferente para múltiplas alternativas, adapte aqui.
            if ',' in alt:
                alt = alt.split(',')[0] 

            variant_info = {'chr': chrom, 'pos': pos, 'ref': ref, 'alt': alt}
            outfile.write(str(variant_info) + '\n')

# --- Como usar o script ---
if __name__ == "__main__":
    # Substitua 'seu_arquivo.vcf' pelo caminho do seu arquivo VCF de entrada
    # e 'variantes_anotadas.txt' pelo nome do arquivo de saída desejado.
    input_vcf = 'file.vcf'  
    output_txt = 'file_var.txt'

    try:
        process_vcf(input_vcf, output_txt)
        print(f"Variantes processadas com sucesso! As informações foram salvas em '{output_txt}'.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_vcf}' não foi encontrado. Verifique o caminho.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
