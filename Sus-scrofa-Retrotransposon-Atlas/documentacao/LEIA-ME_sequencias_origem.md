# Coleção integrada de sequências de retrotransposons

Integração de 1.153 registros anteriores com 549 recebidos do artigo: 454 acrescentados e 95 duplicatas não repetidas. Total: 1.607 registros em 34 arquivos FASTA.

| Classe | Identificadores de origem | Registros FASTA |
|---|---:|---:|
| LINE | 57 | 542 |
| SINE | 135 | 418 |
| PERV | 97 | 580 |
| Outros ERVs | 17 | 61 |
| Transcritos associados a SINE | 3 | 5 |
| Referência 7SLRNA | 1 | 1 |

## Como usar

As pastas LINE, SINE e PERV mantêm os arquivos separados por região. ERV_outros, Referencias_SINE e Referencias_RNA contêm material complementar. A pasta Levantamento contém CSVs delimitados por ponto e vírgula, em UTF-8, com contagens, inventário, manifesto e rastreabilidade de cada integração.

**Unidade principal.** Identificador de origem depurado: modelo/consenso, acesso ou locus. Fragmentos de um mesmo identificador contam uma vez. Não equivale a número de loci biológicos independentes, moléculas únicas ou sequências completas.

**Unidade FASTA.** Cada entrada iniciada por > é um registro. Uma mesma origem pode ter FULL, ORF, UTR, LTR e fragmentos sobrepostos; não somar esses registros como elementos independentes.

**SINE total.** 135 identificadores: 121 no conjunto principal e 14 referências genéricas fornecidas no artigo. A origem suína dessas 14 referências não foi confirmada; para uma figura restrita ao conjunto principal, usar 121 e apresentar as 14 à parte.

**Materiais complementares.** Três transcritos associados a SINE (5 registros FASTA) e uma referência 7SLRNA foram excluídos do total de SINE isolados/consensos. Permanecem no pacote e nas tabelas auxiliares.

**Outros ERVs.** 17 modelos ERV1–ERV18, exceto ERV6, mantidos em ERV_outros. Não foram chamados de PERV. Um modelo inclui a região interna e a LTR, quando fornecidas.

**ERV6A e ERV6B.** Correspondência por coordenadas publicada no artigo: ERV6A = chr5:92185133–92194050; ERV6B = chr9:138895584–138904340. Os loci já constam como PERV-A-5-92.1M e PERV-B-9-138.8M. As novas partes foram acrescentadas sem contar dois novos loci.

**Subtipos PERV.** As classificações PERV-A/PERV-B dos dois loci vêm dos cabeçalhos anteriores. ERV6A/ERV6B são outra nomenclatura do artigo e não uma equivalência universal entre subfamílias. As demais classificações foram mantidas conforme cabeçalho ou log anexo.

**Normalização de nomes.** SscL1A1 e L1A1, por exemplo, representam um identificador; SscSINEA1 e SINEA1_SSc também. Acessos PERV com e sem versão e registros env do mesmo acesso foram agrupados; todas as sequências fornecidas permanecem rastreáveis.

**Duplicatas.** Não se acrescentou uma entrada quando já havia sequência de nucleotídeos idêntica para a mesma origem e a mesma região de destino. FULL idêntico a nao_separadas também foi aproveitado. 95 entradas dispensadas: inclui repetições internas ao novo ZIP. Não se eliminaram fragmentos iguais de origens distintas.

**Preservação.** Os 1.153 registros anteriores foram mantidos, com conteúdo e cabeçalho originais. Acrescentados 454 registros. Apenas o prefixo de pasta foi mantido e os nucleotídeos foram normalizados para maiúsculas e linhas de 80 caracteres. Cabeçalhos novos receberam o DOI de origem.

**Regiões adicionais.** core_sem_polyA não foi convertido em body. TAIL de ERV ficou como remanescente_nao_anotado. LTR isolada não foi duplicada em LTR5/LTR3. FULL de ERV-I representa a sequência interna fornecida, não um provírus completo com duas LTRs.

**Anotações dos fragmentos.** Rótulos ORF/gag/pol/env e coordenadas foram preservados conforme os arquivos recebidos. A conferência checa integridade dos recortes contra FULL; não valida experimentalmente função, atividade ou os limites biológicos dessas regiões. Recortes diferentes da mesma origem coexistem.

**Divergências recebidas.** L1C1 ORF2: 3.803 nt observados versus 3.794 informados. L1D14 ORF2: 3.817 versus 3.818. Os dois recortes divergem do intervalo declarado no FULL. Dados originais preservados, sem correção por suposição. Ver Conferencia.

**Variantes entre pacotes.** Cinco fragmentos anteriores não estão contidos literalmente no novo FULL homônimo: L1A6, SINEA6, SINEA10, SINEB3 e SINEC1. Versões preservadas; os totais por identificador não distinguem variantes de nucleotídeos.

**Cobertura.** Contado apenas material FASTA efetivamente presente nos dois ZIPs. Linhas do log que têm somente coordenadas, links ou FASTA=0 não foram acrescentadas à contagem. A planilha de triagem não foi modificada.

**Figura futura.** Sugestão de unidade para legenda: número de identificadores de origem representados na coleção. Para figura exclusivamente suína: LINE 57, SINE principal 121, PERV 97; manter 14 referências SINE, 17 outros ERVs, 3 transcritos e 7SLRNA em categorias complementares. Não interpretar como abundância genômica.

**Arquivo anterior.** Sequencias_separadas (1)(1).zip

**Arquivo acrescentado.** drive-download-20260712T024928Z-2-001 (1) (1)(1).zip

**Metadados.** TCC_triagem_integrada_PubMed2_com_varredura_sequencias(1).xlsx, aba Log de sequências. Fonte de subtipos de acessos sem classificação no cabeçalho.

**Artigo.** Retrotransposons evolution and impact on lncRNA and protein coding genes in pigs. DOI: 10.1186/s13100-019-0161-8. https://doi.org/10.1186/s13100-019-0161-8 ; PMC6501411, resultados ERV.

**Conferência técnica.** Todos os FASTAs foram lidos; 549 registros recebidos = 454 acrescentados + 95 duplicatas; 1.153 anteriores + 454 = 1.607 finais. Nenhum caractere fora do alfabeto IUPAC aceito foi encontrado. Recortes com start/end comparados em coordenadas 1-based inclusivas.

