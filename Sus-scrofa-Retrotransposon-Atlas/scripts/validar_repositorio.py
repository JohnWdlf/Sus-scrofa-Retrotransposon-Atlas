#!/usr/bin/env python3
"""Valida a coleção FASTA organizada para o repositório do TCC.
Uso: python scripts/validar_repositorio.py
"""
import csv, hashlib, json, collections
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]

def fasta_records(path):
    hdr=None; pieces=[]
    for ln in path.read_text(encoding='utf-8-sig').splitlines():
        line=ln.strip()
        if not line:continue
        if line.startswith('>'):
            if hdr is not None: yield hdr,''.join(pieces).upper()
            hdr=line[1:];pieces=[]
        else: pieces.append(''.join(line.split()))
    if hdr is not None:yield hdr,''.join(pieces).upper()

def main():
    manifest=BASE/'dados/tabelas/manifesto_fasta.csv'
    with manifest.open(encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f, delimiter=';'))
    fasta_files=list((BASE/'dados/FASTA').rglob('*.fasta'))
    cache={f.relative_to(BASE/'dados/FASTA').as_posix():list(fasta_records(f)) for f in fasta_files}
    errors=[]; classes=collections.Counter(); origins=collections.defaultdict(set); visited=set()
    for i,r in enumerate(rows,1):
        key=(r['Arquivo'],int(r['Número no arquivo']))
        if key in visited: errors.append(f'duplicated manifest position: {key}')
        visited.add(key)
        if r['Arquivo'] not in cache or not (1<=key[1]<=len(cache[r['Arquivo']])):
            errors.append(f'missing FASTA position: {key}');continue
        hdr,seq=cache[r['Arquivo']][key[1]-1]
        if not hdr.startswith(r['Cabeçalho de entrada']):errors.append(f'header mismatch: {key}')
        if len(seq)!=int(r['Tamanho (nt)']):errors.append(f'length mismatch: {key}')
        if hashlib.sha256(seq.encode()).hexdigest()!=r['SHA256']:errors.append(f'sequence mismatch: {key}')
        classes[r['Classe']]+=1; origins[r['Classe']].add(r['ID de origem'])
    allpos={(k,i) for k,v in cache.items() for i in range(1,len(v)+1)}
    if visited!=allpos: errors.append(f'missing/extra FASTA positions: {len(allpos-visited)} extra, {len(visited-allpos)} missing')
    out={'arquivos_fasta':len(cache),'registros_fasta':sum(map(len,cache.values())),
         'linhas_manifesto':len(rows),'identificadores':len(set(r['ID de origem'] for r in rows)),
         'por_classe':{c:{'registros_fasta':classes[c],'identificadores':len(origins[c])} for c in sorted(classes)},
         'conjunto_principal':{'registros_fasta':sum(classes[c] for c in ('LINE','SINE','PERV')),
                               'identificadores':sum(len(origins[c]) for c in ('LINE','SINE','PERV'))},
         'inconsistencias_tecnicas':errors}
    target=BASE/'documentacao/verificacao_repositorio.json'
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,ensure_ascii=False,indent=2))
    return 1 if errors else 0

if __name__=='__main__':raise SystemExit(main())
