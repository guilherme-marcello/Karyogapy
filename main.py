from random import randint as rd
from random import choice
from random import sample
import pandas as pd
from time import strftime as stime
from os import getcwd
red = "\033[91;1m"
green = "\033[92;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
cyan = "\033[96;1m"
blue = "\033[94;1m"
ncromo = {1, 2, 5, 11, 13, 14, 15, 16, 19, 20, 21, 22}
caracteristicas = ['Alzheimer', 'Cancro Colorretal', 'Asma', 'Albinismo', 'Cancro de Mama', 'Alzheimer', 'Albinismo e Olhos Castanhos/Azuis', 'Cancro Colorretal e Cerrume e Pigmentação da pele', 'Alzheimer e Olhos Verdes', 'Altura', 'Alzheimer', 'Transtorno Bipolar']


#0 == nulo, 1 == normal, -1 == baixo

def get_cromossomasParentaisDuplos():
    v = [rd(-1,1) for i in range(64)]
    cario = [
    ([[v[0]],[v[1]]], [[v[32]],[v[31]]]),                                                    #C1:  Alzheimer
    ([[v[2]],[v[3]]], [[v[33]],[v[34]]]),                                                    #C2:  CColorretal
    ([[v[4]],[v[5]]], [[v[35]],[v[36]]]),                                                    #C5:  Asma
    ([[v[6]],[v[7]]], [[v[37]],[v[38]]]),                                                    #C11: Albinismo
    ([[v[8]],[v[9]]], [[v[39]],[v[40]]]),                                                    #C13: CMama
    ([[v[10]],[v[11]]], [[v[41]],[v[42]]]),                                                  #C14: Alzheimer
    ([[v[12],v[13]],[v[14],v[15]]], [[v[43],v[44]],[v[45],v[46]]]),                          #C15: Albinismo & Olhos Castanhos/Azuis
    ([[v[16],v[17],v[18]],[v[19],v[20],v[21]]], [[v[47],v[48],v[49]],[v[50],v[51],v[52]]]),  #C16: CColorretal & Cerrume & Cor da Pele
    ([[v[22],v[23]],[v[24],v[25]]], [[v[53],v[54]],[v[55],v[56]]]),                          #C19: Alzheimer & Olhos Verdes
    ([[v[26]],[v[27]]], [[v[58]],[v[59]]]),                                                  #C20: Altura
    ([[v[28]],[v[29]]], [[v[60]],[v[61]]]),                                                  #C21: Alzheimer
    ([[v[30]],[v[31]]], [[v[62]],[v[63]]]),                                                  #C22: TBipolar
]
    return cario


def meioseReducional(cario):
    def profaseI(cario):
        print(green+'[!] INCÍO DA PRÓFASE I')
        for duplosBivalentes,nC in zip(cario,ncromo):
            while True:
                if rd(0,100) <= 35:
                    quiasma = True
                    print(yellow+'[*] HOUVE TROCA DE SEGMENTOS ENTRE CROMATÍDEOS HOMÓLOGOS NÚMERO {0}'.format(nC))
                else:
                    quiasma = False; break
                while quiasma:
                    pontoDeTroca = rd(0,1) #ponto 0 ou ponto 1
                    indexGene0 = rd(0,len(duplosBivalentes[pontoDeTroca][0])-1)
                    indexGene1 = rd(0,len(duplosBivalentes[pontoDeTroca][1])-1)
                    print(yellow+'[*] GENE DA POSIÇÃO {0} NO CROMOSSOMA 1 VAI PARA A POSIÇÃO {1} NO CROMOSSOMA 2 (NO PONTO DE QUIASMA {2})'.format(indexGene0, indexGene1, pontoDeTroca))
                    duplosBivalentes[pontoDeTroca][0][indexGene0], duplosBivalentes[pontoDeTroca][1][indexGene1] = duplosBivalentes[pontoDeTroca][1][indexGene1], duplosBivalentes[pontoDeTroca][0][indexGene0]
                    break
        return cario
        
    def metafaseI(cario):
        print(green+'[!] INÍCIO DA METÁFASE I')
        posicaoPlacaEquatorial = sample([i for i in range(0,len(cario))],len(cario))
        pe = posicaoPlacaEquatorial
        originais = []
        for i in range(0,len(cario)):
            exec('v{0} = pe.index({0}); originais.extend([v{0}]);'.format(i))

        return [cario[pos] for pos in pe], originais
        
    def anafase_telofaseI(cario, posicaoPlaca):
        print(green+'[!] INÍCIO DA ANÁFASE E TELÓFASE I')
        haploideDuplo1, haploideDuplo2 = [],[]
        for duploBivalente in cario:
            qualDuplo = rd(0,1)
            haploideDuplo1.append(duploBivalente[qualDuplo])
            if qualDuplo == 0:
                haploideDuplo2.append(duploBivalente[1])
            else:
                haploideDuplo2.append(duploBivalente[0])
        return (haploideDuplo1, haploideDuplo2), posicaoPlaca
        
    proI = profaseI(cario)
    metaI = metafaseI(proI)
    return anafase_telofaseI(metaI[0],metaI[1])
        

def meioseEquacional(haploidesDuplos, posicaoPlaca):
    def profase_metafaseII(haploidesDuplos, posicaoPlaca):
        print(green+'[!] INÍCIO DA PRÓFASE E METÁFASE II')
        originais2 = [],[]
        posicoesPlaca = sample([i for i in range(0,len(posicaoPlaca))],len(posicaoPlaca)),sample([i for i in range(0,len(posicaoPlaca))],len(posicaoPlaca))
        pe2 = posicoesPlaca
        for idx in [0,1]:
            for i in range(0,len(posicaoPlaca)):
                exec('v{0} = pe2[idx].index({0}); originais2[idx].extend([v{0}]);'.format(i))
        novasposicoes = [[],[]]
        for haploideDuplo,index in zip(haploidesDuplos,[0,1]):
            for pos in posicoesPlaca[index]:
                novasposicoes[index].extend([haploideDuplo[pos]])
        return novasposicoes, originais2
       
    def anafase_telofaseII(novasposicoes,posicoesPlaca):
        print(green+'[!] INÍCIO DA ANÁFASE E TELÓFASE II')
        gametas = [[[],[]],[[],[]]]
       
        for haploDuplo,index in zip(novasposicoes,[0,1]):
            for cromoDuplo in haploDuplo:
                qualgene = sample([0,1],2)
                for idx in [0,1]:      
                    escolha = choice(qualgene)         
                    gametas[index][idx].append(cromoDuplo[escolha])
                    if escolha==0:
                        qualgene.remove(0)
                    else:
                        qualgene.remove(1)
        return gametas, posicoesPlaca
     
    novasposicoes, posicoesPlaca2 = profase_metafaseII(haploidesDuplos, posicaoPlaca)
    return anafase_telofaseII(novasposicoes,posicoesPlaca2)
    
        
            
def get_dicionarios(gametas,posicaoPlaca1,posicaoPlaca2):
    dicionarios = [[[],[]],[[],[]]]
    resultado_meiose = [[{},{}],[{},{}]]
    for mesmaOrigem_gameta,index,dicio in zip(gametas,[0,1], dicionarios):
        posicoes = posicaoPlaca2[index]
        for origem in [0,1]:
            gameta = mesmaOrigem_gameta[origem]   
            dicio[origem] = [gameta[i] for i in posicoes]
    
    for Doisdicionarios,index,updateDict in zip(dicionarios,[0,1],resultado_meiose):
        for dicionario,origem in zip(Doisdicionarios,[0,1]):
            chaves = [i for i in ncromo]
            valores = [dicionario[i] for i in posicaoPlaca1]
            updateDict[origem].update(dict(zip(chaves,valores)))
    return resultado_meiose    
           
def Gametogenese(individuo):
    print(red+'[***] A gerar cromossomas do indivíduo {0}'.format(individuo))
    carioM = get_cromossomasParentaisDuplos()
    print(magenta+'[+] FORMAÇÃO DOS GAMETAS')
    haploidesDuplos, posicaoPlaca1 = meioseReducional(carioM)
    gametas, posicaoPlaca2 = meioseEquacional(haploidesDuplos, posicaoPlaca1)
    resultados = get_dicionarios(gametas,posicaoPlaca1,posicaoPlaca2)
    return resultados

def get_GAMETAdf(resultado_meiose):
    pos_escolhido = choice(sample([0,1,2,3],4))
    for dicionarioGeral,index in zip(resultado_meiose,[1,2]):
        for dicio,origem in zip(dicionarioGeral,[1,2]):
            print(yellow+'[*] {0}º gâmeta originado da célula HAPLÓIDE {1}{2}'.format(origem,index,cyan))
            dataframe = pd.DataFrame(dicio.items(), columns=['Número do cromossoma', 'Atributos'])
            dataframe.insert(1,"Características",caracteristicas)
            print(dataframe)
    if pos_escolhido <= 1:
        escolhido = resultado_meiose[0][pos_escolhido]
    else:
        escolhido = resultado_meiose[1][pos_escolhido-2]
    df_escolhido = pd.DataFrame(escolhido.items(), columns=['Número do par de cromossomas', 'Atributos']); df_escolhido.insert(1,"Características",caracteristicas);
    return df_escolhido, escolhido

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
    if input(blue+'[?] Deseja gravar o DataFrame do cariótipo do bebé como ficheiro csv? (será gravado em {0}) '.format(getcwd())).lower() in ('yes','y','sim','s'):
        now = stime("%Y,%m,%d,%H,%M,%S");t = now.split(',')
        dataframeBEBE.to_csv('cariotipoBEBE'+'_'.join(t)+'.csv')
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
  
