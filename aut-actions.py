import os
import sys
import urllib.request
import json
from pathvalidate import sanitize_filename #limpeza de caracteres especiais
import shutil #mover arquivos

def criaPastas(pastas, nomeProjeto=''):
    nomeProjeto = sanitize_filename(nomeProjeto)
    
    for pasta in pastas:
        nomePasta = os.path.join(nomeProjeto, pasta)
        os.makedirs(nomePasta, True)

def criaArquivos(arquivos, nomeProjeto=''):
    nomeProjeto = sanitize_filename(nomeProjeto)
    for arquivo in arquivos:
        fonte = arquivo["from"]
        destino = arquivo["to"]
        nomeArquivo = fonte.rsplit("/", 1)[-1]
        caminhoCompleto = os.path.join(nomeProjeto, destino, nomeArquivo)

        if not os.path.isfile(caminhoCompleto):
            urllib.request.urlretrieve(fonte, caminhoCompleto)


links = [
    {"from": "http://127.0.0.1:5500/pastaBase/index.html", "to": "src"},
    {"from": "http://127.0.0.1:5500/pastaBase/script.js", "to": "src/js"},
    {"from": "http://127.0.0.1:5500/pastaBase/main.scss", "to": "src/scss"}
    ]

pastas = ['src/scss', 'src/js', 'src/assets']

criaPastas(pastas, 'teste')
criaArquivos(links, 'teste')