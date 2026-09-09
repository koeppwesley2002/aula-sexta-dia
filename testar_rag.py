import json
import os
from pathlib import Path

os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TRANSFORMERS_OFFLINE'] = '1'
nb = json.loads(Path('rag_fenomenologia.ipynb').read_text(encoding='utf-8-sig'))
scope = {}
for i in (4, 6, 8, 10, 12):
    print(f'Executando etapa {i}...', flush=True)
    exec(''.join(nb['cells'][i]['source']), scope)
question = 'O que é intencionalidade, segundo o documento?'
result = scope['responder'](question)
lines = ['# Teste do RAG', '', 'Pergunta: ' + question, '', '## Resposta', '', result['answer'], '', '## Trechos recuperados', '']
assert result['answer'].strip(), 'Resposta vazia'
assert result['context'], 'Nenhum trecho recuperado'
for i, doc in enumerate(result['context'], 1):
    lines.extend([f"### Fonte {i} — página {doc.metadata['page'] + 1}", '', doc.page_content, ''])
Path('TESTE_RAG.md').write_text('\n'.join(lines), encoding='utf-8')
print('\n'.join(lines), flush=True)
