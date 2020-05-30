from assets.cores import *
from assets.constantes import ncromo
from random import randint as rd
from random import choice
from random import sample

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
