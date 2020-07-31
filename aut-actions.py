import os
import sys

def criaPastas(nomeDoProjeto=''):
    
    # estrutura do projeto
    projeto = {
        'src':'index.html', 'src\scss':'main.scss', 'src\js':'script.js'
    }

    # Cria cada pasta da estrutura
    for pasta in projeto:
        
        pastaProjeto = os.path.join(nomeDoProjeto, pasta)
        os.makedirs(pastaProjeto, True)

        #caminho do arquivo que será criado
        caminho = os.path.join(nomeDoProjeto, pasta, projeto[pasta])

        file = open(caminho, 'w')   

criaPastas('teste')