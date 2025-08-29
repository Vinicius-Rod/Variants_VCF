Extrair variantes de um VCF

```bash
import sys
import pandas as pd
```

Processa um arquivo VCF, extrai informações de variantes e as anota em um novo arquivo

```bash
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
```





Lista de variantes de interesse
```bash
variants_of_interest = [
   {'chr': 'chrM', 'pos': 59, 'ref': 'T', 'alt': 'C'},
   {'chr': 'chrM', 'pos': 64, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 72, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 93, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 95, 'ref': 'A', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 103, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 143, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 146, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 150, 'ref': 'CCT', 'alt': 'TCT'},
    {'chr': 'chrM', 'pos': 151, 'ref': 'CTA', 'alt': 'TTA'},
    {'chr': 'chrM', 'pos': 152, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 153, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 182, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 183, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 185, 'ref': 'G', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 186, 'ref': 'C', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 189, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 194, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 195, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 198, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 199, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 200, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 204, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 207, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 228, 'ref': 'G', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 235, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 236, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 247, 'ref': 'GA', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 263, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 271, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 285, 'ref': 'CAA', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 295, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 297, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 310, 'ref': 'TC', 'alt': 'CC'},
    {'chr': 'chrM', 'pos': 316, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 325, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 357, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 456, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 460, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 462, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 489, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 493, 'ref': 'AC', 'alt': 'GC'},
    {'chr': 'chrM', 'pos': 497, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 499, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 513, 'ref': 'GCACA', 'alt': 'GCA'},
    {'chr': 'chrM', 'pos': 567, 'ref': 'A', 'alt': 'ACCC'},
    {'chr': 'chrM', 'pos': 663, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 680, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 709, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 710, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 769, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 825, 'ref': 'T', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 827, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 921, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 930, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 955, 'ref': 'AC', 'alt': 'ACC'},
    {'chr': 'chrM', 'pos': 1018, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 1048, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 1189, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 1243, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 1442, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 1706, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 1719, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 1736, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 1738, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 1811, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 1822, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 1888, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 2092, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 2245, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 2332, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 2352, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 2358, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 2393, 'ref': 'CA', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 2416, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 2758, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 2768, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 2789, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 2885, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 3010, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 3105, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 3197, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 3200, 'ref': 'T', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 3308, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 3396, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 3450, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 3480, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 3505, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 3516, 'ref': 'C', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 3535, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 3547, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 3552, 'ref': 'T', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 3594, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 3666, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 3693, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 3796, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 3866, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 3918, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 4104, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 4158, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 4216, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 4218, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 4232, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 4248, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 4312, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 4336, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 4370, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 4580, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 4586, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 4655, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 4688, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 4715, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 4767, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 4769, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 4820, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 4823, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 4824, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 4883, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 4917, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 4977, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 5027, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 5036, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 5046, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 5096, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 5147, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 5178, 'ref': 'C', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 5231, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 5255, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 5285, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 5331, 'ref': 'C', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 5393, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 5442, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 5460, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 5581, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 5601, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 5603, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 5655, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 5656, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 5773, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 5814, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 5894, 'ref': 'A', 'alt': 'AC'},
    {'chr': 'chrM', 'pos': 5911, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 5951, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 6071, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 6150, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 6185, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 6221, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 6253, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 6260, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 6261, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 6473, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 6524, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 6548, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 6587, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 6663, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 6680, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 6713, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 6755, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 6776, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 6827, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 6917, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 6989, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 7055, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 7076, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 7146, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 7175, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 7196, 'ref': 'C', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 7256, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 7274, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 7337, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 7389, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 7424, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 7498, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 7521, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 7624, 'ref': 'T', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 7697, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 7768, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 7771, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 7789, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 7805, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 7819, 'ref': 'C', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 7867, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 8027, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 8080, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 8206, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 8248, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 8251, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 8270, 'ref': 'CACCCCCTCTACCCCCTCT', 'alt': 'CACCCCCTCT'},
    {'chr': 'chrM', 'pos': 8387, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 8414, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 8428, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 8468, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 8473, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 8527, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 8566, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 8584, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 8618, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 8655, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 8668, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 8697, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 8701, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 8784, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 8794, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 8860, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 8877, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 8932, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 8994, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 9042, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 9055, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 9072, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 9096, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 9221, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 9254, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 9347, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 9377, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 9449, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 9477, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 9540, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 9545, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 9554, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 9698, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 9755, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 9818, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 9950, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 9966, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 10086, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 10115, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 10321, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 10373, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 10398, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 10400, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 10463, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 10550, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 10586, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 10589, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 10664, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 10667, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 10688, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 10792, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 10793, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 10810, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 10819, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 10873, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 10915, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 11002, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 11176, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 11177, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 11251, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 11299, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 11302, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 11440, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 11467, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 11641, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 11654, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 11812, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 11899, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 11914, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 11944, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 12007, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 12019, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 12049, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 12127, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 12236, 'ref': 'GC', 'alt': 'AC'},
    {'chr': 'chrM', 'pos': 12308, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 12372, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 12414, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 12501, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 12519, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 12612, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 12618, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 12633, 'ref': 'C', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 12684, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 12693, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 12696, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 12720, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 12810, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 12948, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 13020, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 13101, 'ref': 'A', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 13105, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 13149, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 13263, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 13276, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 13368, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 13485, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 13506, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 13590, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 13617, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 13650, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 13651, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 13708, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 13789, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 13803, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 13880, 'ref': 'C', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 13886, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 13914, 'ref': 'C', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 13928, 'ref': 'G', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 13934, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 13958, 'ref': 'G', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 13966, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 14000, 'ref': 'T', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 14007, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 14059, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 14127, 'ref': 'A', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 14148, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 14152, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 14167, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 14178, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 14182, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 14203, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 14212, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 14233, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 14284, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 14308, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 14318, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 14470, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 14560, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 14566, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 14569, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 14668, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 14755, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 14769, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 14783, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 14793, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 14798, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 14869, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 14905, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 14911, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 15043, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 15110, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 15115, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 15136, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 15217, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 15226, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 15244, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 15301, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 15311, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 15314, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 15326, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 15431, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 15452, 'ref': 'C', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 15487, 'ref': 'A', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 15514, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 15535, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 15607, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 15629, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 15670, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 15734, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 15784, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 15812, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 15824, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 15849, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 15904, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 15905, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 15924, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 15928, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 15929, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 15930, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 15939, 'ref': 'CT', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 15942, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 15951, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 15978, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16051, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 16069, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16086, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16092, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16093, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16111, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16114, 'ref': 'C', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 16124, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16126, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16129, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 16145, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 16148, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16163, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 16168, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16172, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16178, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16179, 'ref': 'CAAAA', 'alt': 'CAA'},
    {'chr': 'chrM', 'pos': 16182, 'ref': 'AACCCCCT', 'alt': 'ACACCCCCT'},
    {'chr': 'chrM', 'pos': 16183, 'ref': 'ACCCC', 'alt': 'CCCCC'},
    {'chr': 'chrM', 'pos': 16185, 'ref': 'C', 'alt': '*'},
    {'chr': 'chrM', 'pos': 16187, 'ref': 'CCT', 'alt': 'TCT'},
    {'chr': 'chrM', 'pos': 16188, 'ref': 'CT', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16189, 'ref': 'TCCC', 'alt': 'ACCC'},
    {'chr': 'chrM', 'pos': 16192, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16209, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16213, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 16215, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 16217, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16224, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16230, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 16234, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16241, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 16249, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16256, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16259, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16261, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16264, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16265, 'ref': 'A', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16266, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16270, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16274, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 16278, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16286, 'ref': 'C', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 16290, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16291, 'ref': 'C', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 16292, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16293, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 16294, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16295, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16296, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16298, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16304, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16309, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 16311, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16312, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 16319, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 16320, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16325, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16327, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16344, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16355, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16356, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16360, 'ref': 'C', 'alt': 'T'},
    {'chr': 'chrM', 'pos': 16362, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16368, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16390, 'ref': 'G', 'alt': 'A'},
    {'chr': 'chrM', 'pos': 16399, 'ref': 'A', 'alt': 'G'},
    {'chr': 'chrM', 'pos': 16468, 'ref': 'T', 'alt': 'C'},
    {'chr': 'chrM', 'pos': 16527, 'ref': 'C', 'alt': 'T'}]
```

Nome do arquivo VCF

```bash
vcf_file = 'file.vcf'
```

Lista para armazenar os resultados

```bash
results = []

try:
    with open(vcf_file, 'r') as f:
        header = []
        for line in f:
            if line.startswith('#'):
                if line.startswith('#CHROM'):
                    header = line.strip().split('\t')  # Captura a linha de cabeçalho com nomes das amostras
                continue  # Pula outras linhas de cabeçalho do arquivo VCF

            fields = line.strip().split('\t')
            chrom = fields[0]
            position = int(fields[1])
            ref_allele = fields[3]
            alt_alleles = fields[4].split(',')
            quality = fields[5]
            info = fields[7]

            # Verifica se a linha corresponde a qualquer variante de interesse
            for variant in variants_of_interest:
                if chrom == 'chrM' and position == variant['pos'] and ref_allele == variant['ref'] and variant['alt'] in alt_alleles:
                    # Encontrou a variante de interesse, agora obter os genótipos dos indivíduos
                    genotypes = fields[9:]  # Os genótipos começam a partir da coluna 10 (índice 9)

                    # Salva os genótipos dos indivíduos que são 0/1, 1/0, ou 1/1
                    for i, genotype in enumerate(genotypes):
                        sample_name = header[i + 9]  # Nomes das amostras começam na coluna 10 (índice 9)
                        genotype_value = genotype.split(':')[0]
                        if genotype_value in ['0/1', '1/0', '1/1']:
                            results.append({
                                'SampleID': sample_name,
                                'Position': position,
                                'Reference': ref_allele,
                                'Mutated_Allele': variant['alt'],
                                'Quality': quality,
                                'Info': info,
                                'Genotype_Type': genotype_value
                            })

except FileNotFoundError:
    print(f"Arquivo {vcf_file} não encontrado.")
    sys.exit(1)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    sys.exit(1)
```

Cria um DataFrame a partir dos resultados

```bash
df = pd.DataFrame(results)
```

Salva os resultados em um arquivo Excel

```bash
output_file = 'file.xlsx'
df.to_excel(output_file, index=False)

print(f"Resultados salvos em {output_file}")
```

