from reproducaoSexuada.meiose import *
from reproducaoSexuada.replicacaoSemiConservativa import *
from assets.cores import *
from assets.constantes import caracteristicas
from random import sample
import pandas as pd

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
