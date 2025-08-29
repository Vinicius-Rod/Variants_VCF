Extrair variantes de um VCF

```bash
import sys
import pandas as pd
```

Processa um arquivo VCF, extrai informações de variantes e as anota em um novo arquivo

```bash
def process_vcf(input_vcf_path, output_txt_path):
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

if __name__ == "__main__":
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
   {'chr': 'chrM', 'pos': 64, 'ref': 'C', 'alt': 'T'}]
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

