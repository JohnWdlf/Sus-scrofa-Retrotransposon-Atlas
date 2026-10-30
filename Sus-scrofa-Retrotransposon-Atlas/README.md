# Curadoria de retrotransposons de *Sus scrofa*

Coleção documental de sequências de DNA e metadados relativos a LINEs, SINEs e retrovírus endógenos suínos (PERVs), organizada como base para a construção de um atlas genômico.

## Conteúdo

- **34 arquivos FASTA**, contendo **1.607 registros** de sequências recuperadas.
- **310 identificadores de origem** (modelos, consensos, acessos ou loci), dos quais **275** pertencem ao conjunto principal LINE/SINE/PERV e **35** são materiais complementares.
- Diretório `dados/FASTA/`: arquivos distribuídos pelas classes e regiões estruturais, incluindo os materiais complementares da coleção auditada.
- Diretório `dados/tabelas/`: manifesto FASTA, inventário de origens, contagens, integração e registros de conferência em CSV.
- Diretório `metadados/`: planilhas de levantamento e triagem.
- Diretório `documentacao/`: dicionário de campos, notas originais e auditoria.
- Diretório `scripts/`: script de auditoria preservado no pacote suplementar.

## Como localizar um registro

1. Consultar `dados/tabelas/manifesto_fasta.csv`.
2. Localizar a coluna **ID de origem** ou **Cabeçalho de entrada**.
3. Usar as colunas **Arquivo** e **Número no arquivo** para encontrar o registro FASTA correspondente dentro de `dados/FASTA/`.
4. Usar `metadados/Triagem_integrada.xlsx`, aba **Log de sequências**, para localizar os dados bibliográficos disponíveis; atenção: nem toda entrada do manifesto tem associação bibliográfica individual conferida.

**Unidades de contagem:** identificadores de origem não são sinônimos de registros FASTA. Fragmentos de uma origem podem aparecer em vários arquivos.

## Escopo e limitações

Esta coleção apresenta sequências publicadas, metadados e recortes estruturais; não demonstra atividade biológica e não equivale a uma nova anotação genômica exaustiva. Existem pendências documentadas de correspondência entre recortes e algumas sequências de referência. O campo `Origem` no manifesto identifica, em alguns casos, apenas o conjunto de integração (`Anterior` ou `Artigo 2019`), não necessariamente o artigo primário individual.

## Verificação

Os arquivos FASTA foram contados neste pacote: **34 arquivos**, **1.607 entradas iniciadas por `>`**. Para a conferência documental histórica, consultar `documentacao/auditoria.json` e `scripts/auditar_colecao.py`.

## Proveniência e condições de reutilização

Sequências e dados foram reunidos de publicações, suplementos e repositórios. Atribuições bibliográficas individuais e condições de reutilização devem ser conferidas nas fontes originais antes da divulgação pública. **Este pacote não estabelece uma licença geral de redistribuição para dados de terceiros.** Até a conclusão dessa revisão, recomenda-se manter o repositório privado, se necessário, e publicá-lo somente após verificar permissões e atribuições.

## Como citar

Antes de divulgação formal, preencher autoria, instituição, ano, versão e identificação persistente do conjunto (por exemplo, DOI de uma versão publicada). O README não constitui uma referência bibliográfica definitiva.
