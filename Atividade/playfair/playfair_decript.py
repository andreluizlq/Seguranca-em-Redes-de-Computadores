f1=input("Frase: ")
cc=input("Chave: ")
c=cc.upper()
frase=[]
chaveorig=[]
chave=[]


##========================================================
# LAÇO PARA ADICIONAR A FRASE ACIMA f1 NO VETOR frase
# O SEGUNDO LAÇO É PRA ARMAZENAR c NO VETOR chaveorig

for i in range(len(f1)):
    frase.append(f1[i])
for i in range(len(c)):
    chaveorig.append(c[i])




##============================================
## LAÇO PARA TIRAR AS LETRAS IGUAIS DO VETOR chaveorig

a=1
for i in chaveorig:
    for j in range(a,len(chaveorig)):
        if chaveorig[j]==i:
            chaveorig[j]='#'
    a+=1

for i in range(len(chaveorig)):
    if chaveorig[i]=='#':
        continue
    else:
        chave.append(chaveorig[i])

    

##=========================================================
# A PARTE ABAIXO CRIA UM VETOR COM 25 INDICES, SENDO QUE O
# 'J' FOI DELETADO, ASSIM SENDO O 'I' SERÁ CONSIDERADO AMBAS
# AS LETRAS

matriz=[]
for i in range(len(chave)):
    matriz.append(chave[i])

nums=65

for i in range(25):
    if nums==74:
        nums+=1
    if chr(nums) in matriz:
        nums+=1
        continue
    else:
        matriz.append(chr(nums))
        nums+=1


##========================================================
# ABAIXO FOI CRIADO UMA MATRIZ DE FATO 5X5, COM OS MESMOS
# DADOS DO PASSO ANTERIOR, UNICA DIFERENÇA É QUE ANTES ERA
# UM VETOR


matrizz=[]
cont1=0
for i in range(5):
    linha=[]
    for j in range(5):
        linha.append(matriz[cont1])
        cont1+=1
    matrizz.append(linha)



#### PRINTAR MATRIZ ATUAL BONITINHA
##for i in range(5):
##    print(matrizz[i])
##
##for i in range(len(frase)):
##    print(frase[i],end="")
##print()





## CONTINUANDO O CODIGO

cript=[]
for i in range(0,len(frase),3):
    let1=i
    let2=i+1

    vetor1=[]
    vetor2=[]
    
    # LAÇO PARA ADICIONAR EM vetor1, vetor2 OS INDICES
    # ENCONTRADOS DE CADA PAR NA MATRIZ... EX: 'SE'
    # AS COORDENADAS DE 'S' ESTÁ EM vetor1 E DE 'E'
    # EM vetor2
    for j in range(5):
        for k in range(5):
            if frase[let1]==matrizz[j][k]:
                vetor1.append(j)
                vetor1.append(k)
            if frase[let2]==matrizz[j][k]:
                vetor2.append(j)
                vetor2.append(k)
    
    # CONDIÇÃO PARA SABER SE ESTÁ NA MESMA LINHA
    # SE SIM, ANDA UMA CASA PARA ESQUERDA.
    if vetor1[0]==vetor2[0]:
        vetor1[1]=vetor1[1]-1
        vetor2[1]=vetor2[1]-1
        if vetor1[1]<0:
            vetor1[1]=vetor1[1]+5
        if vetor2[1]<0:
            vetor2[1]=vetor2[1]+5
        cript.append(matrizz[vetor1[0]][vetor1[1]])
        cript.append(matrizz[vetor2[0]][vetor2[1]])

    # CONDIÇÃO PARA SABER SE ESTÁ NA MESMA COLUNA
    # SE SIM, SOBE UMA CASA
    elif vetor1[1]==vetor2[1]:
        vetor1[0]=vetor1[0]-1
        vetor2[0]=vetor2[0]-1
        if vetor1[0]<0:
            vetor1[0]=vetor1[0]+5
        if vetor2[0]<0:
            vetor2[0]=vetor2[0]+5
        cript.append(matrizz[vetor1[0]][vetor1[1]])
        cript.append(matrizz[vetor2[0]][vetor2[1]])


    # CONDIÇÃO PARA QUANDO NÃO ESTÃO NA MESMA LINHA
    # NEM NA MESMA COLUNA. NESSE CASO, TROCA APENAS
    # A COLUNA DE AMBOS
    else:
        aux=vetor1[0]
        vetor1[0]=vetor2[0]
        vetor2[0]=aux
        cript.append(matrizz[vetor1[0]][vetor1[1]])
        cript.append(matrizz[vetor2[0]][vetor2[1]])


## PRINTA A MENSSAGEM DECRIPTADA EM DIGRAMAS (IGNORE
## QUALQUER 'W' QUE APAREÇA)
contFinal=0
for i in range(len(cript)):
    if contFinal==2:
        print(" {}".format(cript[i]),end="")
        contFinal=1
    else:
        print(cript[i],end="")
        contFinal+=1

