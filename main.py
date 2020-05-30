from reproducaoSexuada.gametogenese import *
from assets.constantes import *
from assets.cores import *
from random import choice
import pandas as pd
from time import strftime as stime
from os import getcwd

def main():
    carioM = Gametogenese('MASCULINO')
    gametaMasculino = get_GAMETAdf(carioM);
    if choice([0,1]) == 0:
        boy = True
    else:
        girl = True; boy=False;
    print(magenta+'[+] O GÁMETA MASCULINO ESCOLHIDO FOI: {0}{1}'.format(gametaMasculino[1],cyan))
    print(gametaMasculino[0])
    
    carioF = Gametogenese('FEMININO')
    gametaFeminino = get_GAMETAdf(carioF)
    print(magenta+'[+] O GÁMETA FEMININO ESCOLHIDO FOI: {0}{1}'.format(gametaFeminino[1],cyan))
    print(gametaFeminino[0])
    
    print('\n'+red+'[***] A inicializar o processo de CARIOGAMIA dos gâmetas selecionados...\n')
    if boy:
        print(magenta+"[+] O GÂMETA MASCULINO TRAZ UM CROMOSSOMA SEXUAL Y."); print(green+"[!] É UM RAPAZ!"); cromoSex = ['Y','X']
    else:
        print(magenta+"[+] O GÂMETA MASCULINO TRAZ UM CROMOSSOMA SEXUAL X."); print(green+"[!] É UM RAPARIGA!"); cromoSex = ['X','X']
    chaves = [i for i in ncromo]
    valores = []
    cariotipodobebe = {}
    for genePAI,geneMAE in zip(gametaMasculino[1].values(),gametaFeminino[1].values()):
        valores.append([genePAI,geneMAE])
    cariotipodobebe.update(dict(zip(chaves,valores)))
    dataframeBEBE = pd.DataFrame(cariotipodobebe.items(), columns=['Número do par de cromossomas', 'Atributos'])
    dataframeBEBE.insert(1,"Características",caracteristicas)
    dataframeBEBE = dataframeBEBE.append({'Número do par de cromossomas':23,'Características':'Cromossomas Sexuais','Atributos':cromoSex},ignore_index=True)	
    print(cyan,dataframeBEBE)
    if input(blue+'[?] Deseja gravar o DataFrame do cariótipo do bebé como ficheiro csv? (será gravado em {0}/OUTPUT) '.format(getcwd())).lower() in yes:
        now = stime("%Y,%m,%d,%H,%M,%S");t = now.split(',')
        dataframeBEBE.to_csv('OUTPUT/cariotipoBEBE'+'_'.join(t)+'.csv')
    else:
        print(red+"[!!!] O programa será encerrado...")
        exit(0)

try:
    if __name__ == '__main__':
        main()
except KeyboardInterrupt:
    print("\n")
    print(red + "[!!!] KeyboardInterrupt Detetado")
    print(red + "[!!!] RIP")
    exit(0)
