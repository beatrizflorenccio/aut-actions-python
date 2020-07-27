import os
import sys
import shutil

def criaPastas(nomeDoProjeto=''):
    
    # estrutura do projeto
    estrutura = ['src', 'src\scss', 'src\js']

    # Cria cada pasta da estrutura
    num_pasta = 0
    for pasta in estrutura:
        
        pastaProjeto = os.path.join(nomeDoProjeto, pasta)
        os.makedirs(pastaProjeto, True)

        # Arquivos criados
        arquivos = ['index.html', 'main.scss', 'script.js']

        file = open(arquivos[num_pasta], 'w')
        num_pasta += 1

               

criaPastas('teste')