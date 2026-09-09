# RAG gratuito com o PDF Fenomenologia

RAG (Geração Aumentada por Recuperação) combina a busca em documentos com um modelo de linguagem. É semelhante a uma prova com consulta: o sistema seleciona trechos do PDF antes de elaborar a resposta. Isso ajuda a fundamentar a resposta, mas não elimina possíveis erros do modelo.

## Fluxo do trabalho

```text
Fenomenologia.pdf → extração do texto → divisão em trechos
                                             ↓
                                 embeddings locais → Chroma
                                                        ↑ busca
Pergunta → embedding da pergunta → trechos relevantes ───┘
                                         ↓
                         pergunta + contexto + instruções
                                         ↓
                               modelo de linguagem local
                                         ↓
                               resposta + fontes consultadas
```

## Como o RAG funciona na prática

1. **Recuperação (Retrieval):** o sistema transforma a pergunta em um vetor e busca os trechos mais próximos no banco Chroma.
2. **Aumento (Augmentation):** os trechos recuperados são acrescentados à pergunta e às instruções para formar o prompt.
3. **Geração (Generation):** o modelo local gera uma resposta em português a partir desse contexto. O notebook mostra também as páginas e os trechos consultados para conferência.

## Implementação

O documento é `Fenomenologia.pdf`. Os embeddings usam `paraphrase-multilingual-MiniLM-L12-v2`; a geração usa `Qwen3-0.6B`. Ambos executam na CPU. Não é necessária chave de API nem pagamento por chamadas. A primeira execução precisa de internet para baixar as bibliotecas e os modelos; os downloads podem ocupar alguns GB e levar vários minutos.

O banco fica em `db_fenomenologia_rag`, separado dos experimentos anteriores. Os identificadores dos trechos são determinísticos e a coleção depende do conteúdo do PDF, permitindo repetir a indexação sem duplicar os mesmos trechos.

## Como executar

Abra `rag_fenomenologia.ipynb` no VS Code, selecione seu kernel Python e execute as células em ordem. Se a instalação pedir reinicialização, reinicie o kernel e continue na célula de imports. Na última célula, altere `pergunta` para consultar o documento.

## Limitações

O modelo de geração é pequeno para permitir execução local: pode produzir respostas incompletas ou incorretas. Confira as fontes exibidas. A busca sempre retorna os trechos mais próximos, mesmo quando não há uma resposta adequada; a instrução de admitir falta de informação não é uma garantia. PDFs digitalizados como imagem precisam de OCR, não incluído neste trabalho. As páginas exibidas são as posições no arquivo PDF, não necessariamente a numeração impressa.

## Referências técnicas

- [Embeddings locais com LangChain](https://docs.langchain.com/oss/python/integrations/embeddings/sentence_transformers)
- [Modelos multilíngues Sentence Transformers](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html)
- [Modelo Qwen3-0.6B e instruções de uso](https://huggingface.co/Qwen/Qwen3-0.6B)
