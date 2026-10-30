"""Auditoria documental realizada na revisão de 26/10/2026.

Não refaz a busca bibliográfica nem a integração histórica dos dois pacotes.
Confere o pacote final contra seu manifesto e conta decisões da planilha.
Uso: python auditar_colecao.py --colecao Sequencias_separadas_integradas.zip
     --triagem TCC_triagem_integrada.xlsx --saida auditoria
Requer Python 3 e openpyxl para a opção --triagem.
"""
import argparse, collections, csv, hashlib, io, json, platform, sys, zipfile
from pathlib import Path

def fasta(text):
    header=None; seq=[]
    for line in text.splitlines():
        line=line.strip()
        if not line: continue
        if line.startswith('>'):
            if header is not None: yield header, ''.join(seq).upper()
            header=line[1:];seq=[]
        else:seq.append(''.join(line.split()))
    if header is not None:yield header, ''.join(seq).upper()

def audit(colecao,triagem=None):
    result={'data_da_revisao':'2026-10-26','python':platform.python_version()}
    with zipfile.ZipFile(colecao) as z:
        prefix='Sequencias_separadas/'
        manifest=list(csv.DictReader(io.StringIO(z.read(prefix+'Levantamento/manifesto_fasta.csv').decode('utf-8-sig')),delimiter=';'))
        files={n[len(prefix):]:list(fasta(z.read(n).decode('utf-8-sig'))) for n in z.namelist() if n.lower().endswith(('.fasta','.fas','.fna','.fa'))}
        errors=[]; origins=collections.defaultdict(set); byclass=collections.Counter(); byregion=collections.Counter()
        for row in manifest:
            h,s=files[row['Arquivo']][int(row['Número no arquivo'])-1]
            if len(s)!=int(row['Tamanho (nt)']):errors.append(['comprimento',row['Arquivo'],row['Número no arquivo']])
            if hashlib.sha256(s.encode()).hexdigest()!=row['SHA256']:errors.append(['sha256',row['Arquivo'],row['Número no arquivo']])
            if set(s)-set('ACGTRYSWKMBDHVN'):errors.append(['alfabeto',row['Arquivo'],row['Número no arquivo']])
            if not h.startswith(row['Cabeçalho de entrada']):errors.append(['cabecalho',row['Arquivo'],row['Número no arquivo']])
            byclass[row['Classe']]+=1;origins[row['Classe']].add(row['ID de origem']);byregion[(row['Classe'],row['Região'])]+=1
        result.update({'arquivos_fasta':len(files),'registros_fasta':sum(map(len,files.values())),'linhas_manifesto':len(manifest),'identificadores':len(set(r['ID de origem'] for r in manifest)),'por_classe':{k:{'identificadores':len(v),'registros_fasta':byclass[k]} for k,v in origins.items()},'divergencias_manifesto':errors})
        result['origens_de_integracao']={key:{'identificadores':len(set(r['ID de origem'] for r in manifest if r['Origem']==key)),'registros_fasta':sum(r['Origem']==key for r in manifest)} for key in sorted(set(r['Origem'] for r in manifest))}
    if triagem:
        import openpyxl
        result['openpyxl']=openpyxl.__version__
        w=openpyxl.load_workbook(triagem,read_only=True,data_only=True)
        rows=list(w['Triagem'].values);rows=[r for r in rows[1:] if r[1]]
        result['triagem']={'registros':len(rows)}
        for key,idx in [('titulo_resumo',3),('texto_completo',4),('extracao',5),('evidencia',17)]:
            counts=collections.Counter(r[idx] for r in rows)
            result['triagem'][key]={str(k):v for k,v in counts.items()}
        result['triagem']['selecionados_sem_decisao_texto']=sum(r[3]==1 and r[4] is None for r in rows)
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--colecao',required=True);ap.add_argument('--triagem');ap.add_argument('--saida',required=True);args=ap.parse_args()
    out=Path(args.saida);out.mkdir(parents=True,exist_ok=True)
    result=audit(args.colecao,args.triagem)
    (out/'auditoria.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    sys.exit(1 if result['divergencias_manifesto'] else 0)
