# Organizador de Arquivos em Python

Script em Python que organiza arquivos automaticamente em subpastas, separando-os por extensão. Feito para praticar a biblioteca `os`.

## O que o script faz

1. Sorteia nomes de arquivos com extensões variadas (jpg, txt, pdf, docx, mp4)
2. Cria uma pasta para cada tipo de extensão
3. Cria os arquivos de teste
4. Move cada arquivo para sua pasta correspondente

## Bibliotecas usadas

- `os` — criar pastas (`os.makedirs`), listar arquivos (`os.listdir`), mover/renomear (`os.rename`), verificar existência (`os.path.exists`) e remover arquivos (`os.remove`)
- `random` — sortear nomes e extensões (`random.choice`)

## Como rodar

```bash
python main.py
```

Depois de rodar, os arquivos vão aparecer organizados dentro das pastas `jpg/`, `txt/`, `pdf/`, `docx/` e `mp4/`.

## Estrutura do projeto

```
main.py
jpg/
txt/
pdf/
docx/
mp4/
```
