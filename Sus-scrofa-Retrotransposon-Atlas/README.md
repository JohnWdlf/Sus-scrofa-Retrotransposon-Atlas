# Curadoria de retrotransposons de *Sus scrofa*

Coleção documental de sequências nucleotídicas e metadados de LINEs, SINEs e retrovírus endógenos suínos (PERVs), organizada por classe, subtipo, identificador de origem e região estrutural. Este repositório corresponde ao conjunto de dados utilizado no Trabalho de Conclusão de Curso da Pontifícia Universidade Católica do Paraná (PUCPR), 2026.

## Composição da coleção

| Categoria | Identificadores de origem | Registros FASTA |
|---|---:|---:|
| LINE | 57 | 542 |
| SINE | 121 | 404 |
| PERV | 97 | 580 |
| **Conjunto principal** | **275** | **1.526** |
| Outros ERVs | 17 | 61 |
| Referências genéricas de SINE | 14 | 14 |
| Transcritos associados a SINE | 3 | 5 |
| Referência 7SLRNA | 1 | 1 |
| **Coleção completa** | **310** | **1.607** |

Os 34 arquivos FASTA organizam os registros por **classe e região estrutural**. Cada arquivo pode conter múltiplos identificadores e subtipos. O agrupamento por **subtipo** é realizado pelo inventário, pela planilha de levantamento e pelos índices CSV. Um identificador de origem pode reunir várias sequências integrais e seus fragmentos; não equivale necessariamente a uma inserção genômica independente.

## Organização dos dados

```text
dados/
├── FASTA/
│   ├── LINE/                 (8 arquivos FASTA)
│   ├── SINE/                 (6 arquivos FASTA)
│   ├── PERV/                 (13 arquivos FASTA)
│   ├── ERV_outros/           (5 arquivos FASTA; complementar)
│   ├── Referencias_SINE/     (1 arquivo FASTA; complementar)
│   └── Referencias_RNA/      (1 arquivo FASTA; complementar)
├── planilhas/
│   └── Levantamento_LINE_SINE_PERV.xlsx
├── tabelas/
│   ├── manifesto_fasta.csv
│   ├── inventario_origens.csv
│   ├── contagens_regioes.csv
│   ├── integracao_artigo.csv
│   ├── conferencia_recortes.csv
│   └── [tabelas auxiliares de classes e subtipos]
└── indices/
    ├── LINE.csv
    ├── SINE.csv
    ├── PERV.csv
    └── Material_complementar.csv
metadados/
    Triagem_integrada.xlsx
    correspondencia_suplementos.csv
documentacao/
    dicionario_campos.csv
    auditoria_original.json
    verificacao_repositorio.json
scripts/
    validar_repositorio.py
    auditar_colecao_original.py
```

A planilha `dados/planilhas/Levantamento_LINE_SINE_PERV.xlsx` possui as abas **Resumo, Subtipos, Origens, Regioes, Conferencia e Metodo**, com a organização descrita no TCC. A planilha `metadados/Triagem_integrada.xlsx` mantém o levantamento bibliográfico e o log de sequências.

### Regiões estruturais

- **LINE:** 5′ UTR, ORF1, região intergênica, ORF2, 3′ UTR, cauda, sequências integrais fornecidas e não separadas.
- **SINE:** cabeça (*head*), corpo (*body*), cauda (*tail*), núcleo sem poli(A), integrais fornecidas e não separadas.
- **PERV:** LTRs, *gag*, *pol*, *env*, outras ORFs, UTRs, intergênicas, integrais fornecidas e não separadas.
- **Complementares:** outros ERVs, referências genéricas de SINE, transcritos associados a SINE e referência 7SLRNA.

Os **cinco transcritos associados a SINE** são identificados como material complementar no manifesto, mas permanecem fisicamente nos arquivos da pasta `dados/FASTA/SINE/`. Eles são apresentados em `dados/indices/Material_complementar.csv`, sem cópias adicionais. Por essa razão, a pasta SINE contém 409 entradas físicas, mas somente 404 integram o conjunto principal.

## Identificadores e rastreabilidade

O arquivo `dados/tabelas/manifesto_fasta.csv` fornece, para cada registro, as colunas **Arquivo**, **Número no arquivo**, **Origem**, **Classe**, **Subtipo**, **ID de origem**, **Região**, **Tamanho (nt)**, **SHA256** e **Cabeçalho de entrada**. Os caminhos na coluna `Arquivo` são relativos a `dados/FASTA/`, sem alteração em relação ao manifesto da coleção original. O subtipo e a região de cada entrada podem ser consultados também nos arquivos de `dados/indices/`.

O exemplo descrito no TCC, `LINE/LINE_ORF1.fasta`, entrada 50, continua localizável em `dados/FASTA/LINE/LINE_ORF1.fasta`, preservando o cabeçalho, a sequência e sua posição.

## Procedência e verificação

Os dados vieram de publicações científicas, repositórios e materiais suplementares. O arquivo `metadados/correspondencia_suplementos.csv` documenta associações bibliográficas de nomes internos de suplementos a artigos identificados, com o grau de confirmação disponível. Os registros originais de proveniência foram preservados.

A conferência técnica do repositório compara todas as sequências com o manifesto, verificando posição, comprimento e correspondência dos cabeçalhos e sequências. O resultado está em `documentacao/verificacao_repositorio.json`. A auditoria histórica da coleção permanece em `documentacao/auditoria_original.json`.

Esta coleção não corresponde a uma nova anotação exaustiva do genoma suíno e não permite inferir abundância genômica ou atividade biológica. Permanecem pendências documentadas de correspondência entre alguns fragmentos e sequências integrais. Os dados de terceiros continuam sujeitos às condições de uso das fontes originais; este repositório não declara uma licença geral sobre materiais de terceiros.

## Identificação do trabalho

**Título do TCC:** Caracterização genômica de *Sus scrofa* para construção de um atlas de elementos transponíveis  
**Autores:** Ana Carolina Huebl Januário; João Victor Muller da Silva; Julia Carneiro Camargo  
**Orientador:** Prof. Andrey Cabral Meira  
**Instituição:** Pontifícia Universidade Católica do Paraná (PUCPR) — Biotecnologia  
**Ano:** 2026  
**Versão documental:** 1.0
