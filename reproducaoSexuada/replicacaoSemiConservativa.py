from random import randint as rd

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
