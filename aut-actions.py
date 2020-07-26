import os
import sys
import urllib.request
import json
from pathvalidate import sanitize_filename #limpeza de caracteres especiais
import shutil #mover arquivos

def criaPastas(pastas, nomeProjeto=''):
    global nomeProjetoLimpo 
    nomeProjetoLimpo = sanitize_filename(nomeProjeto)
    
    for pasta in pastas:
        nomePasta = os.path.join(nomeProjetoLimpo, pasta)
        os.makedirs(nomePasta, True)

def criaArquivos(arquivos):
    for arquivo in arquivos:
        open(arquivo, 'x')
    
        if '.html' in arquivo:
            pasta = "src"
            destino = os.path.join(nomeProjetoLimpo, pasta)
            shutil.move(arquivo, destino)

        if '.scss' in arquivo:
            pasta = "src/scss"
            destino = os.path.join(nomeProjetoLimpo, pasta)
            shutil.move(arquivo, destino)

        if '.js' in arquivo:
            pasta = "src/js"
            destino = os.path.join(nomeProjetoLimpo, pasta)
            shutil.move(arquivo, destino)

pastas = ['src/scss', 'src/js', 'src/assets']
arquivos = ['index.html', 'main.scss', 'script.js']

criaPastas(pastas, 'teste')
criaArquivos(arquivos)